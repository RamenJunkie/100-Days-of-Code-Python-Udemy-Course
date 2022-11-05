from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hdufDFDSj22k34sSdfhjas9s'
Bootstrap(app)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy(app)

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = SelectField('Rating', choices=[('10'), ('9'), ('8'), ('7'), ('6'), ('5'), ('4'), ('3'), ('2'), ('1')],
                         validators=[DataRequired()])
    submit = SubmitField('Add Book')

class EditForm(FlaskForm):
    new_rating = SelectField('Rating', choices=[('10'), ('9'), ('8'), ('7'), ('6'), ('5'), ('4'), ('3'), ('2'), ('1')],
                         validators=[DataRequired()])
    submit = SubmitField('Edit Book')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

@app.route('/delete<book_id>')
def delete_book(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect('/')

@app.route('/edit<book_id>', methods=['GET', 'POST'])
def edit(book_id):
    form = EditForm()
    if form.validate_on_submit():
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = int(form.new_rating.data)
        db.session.commit()
        return redirect('/')

    return render_template('edit.html', form=form)

@app.route('/')
def home():
    db.create_all()
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(title=form.title.data, author=form.author.data, rating=form.rating.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect('/')

    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)


