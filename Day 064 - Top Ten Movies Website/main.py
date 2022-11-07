from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import requests
from auth import *

tmdb_api_url = f"https://api.themoviedb.org/3/search/movie?api_key={tmdb_key}&language=en-US&page=1&include_adult=false&query="

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBfdsafsdaghfgbshBXor23f2sKR6b'
Bootstrap(app)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top_movies.db"
db = SQLAlchemy(app)

def check_rating(form, field):
    rating = field.data
    try:
        rating = float(rating)
    except ValueError:
        raise ValidationError(u'Rating Must be a number between 0 and 10.')
    if rating > 10 or rating < 0:
        raise ValidationError(u'Rating Must be a number between 0 and 10.')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), unique=True, nullable=False)
    img_url = db.Column(db.String(250), unique=True, nullable=False)


class EditForm(FlaskForm):
    new_rating = StringField('Rating', validators=[check_rating])
    new_review = StringField("Review")
    submit = SubmitField('Edit Movie')

class MovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    rating = StringField('Rating (0-10)', validators=[DataRequired(), check_rating])
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
    db.create_all()
    all_movies = db.session.query(Movie).order_by(Movie.rating.desc()).all()
    return render_template("index.html", movies= all_movies)

@app.route('/edit<id>', methods=['GET', 'POST'])
def edit(id):
    form = EditForm()
    movie_to_update = Movie.query.get(id)
    if form.validate_on_submit():
        movie_to_update = Movie.query.get(id)
        movie_to_update.rating = float(form.new_rating.data)
        movie_to_update.review = form.new_review.data
        db.session.commit()
        return redirect('/')

    return render_template('edit.html', form=form, movie = movie_to_update)

@app.route('/delete<id>')
def delete(id):
    to_delete = Movie.query.get(id)
    db.session.delete(to_delete)
    db.session.commit()
    return redirect('/')

@app.route("/add", methods=['GET', 'POST'])
def add():
    global result_data
    global user_rating
    global review_text
    form = MovieForm()
    if form.validate_on_submit():
        result = requests.get(url=f"{tmdb_api_url}{form.title.data}")
        result.raise_for_status()
        user_rating = form.rating.data
        review_text = form.review.data
        result_data = result.json()
        # print(result_data['results'])
        return render_template('select.html', movie_results = result_data['results'])
    return render_template('add.html', form=form)

@app.route("/insert<which>")
def insert_new(which):
    global result_data
    global user_rating
    global review_text

    print(result_data)
    payload = result_data['results'][int(which)]
    title = payload['title']
    description = payload['overview']
    img_url = "https://image.tmdb.org/t/p/w500"+payload['poster_path']
    year = int(payload['release_date'][0:4])
    #print(img_url+" "+str(year)+" "+description)
    new = Movie(title=title, description = description, rating=user_rating, img_url=img_url, year=year, ranking= 10, review = review_text)
    db.session.add(new)
    db.session.commit()
    return redirect('/')





if __name__ == '__main__':
    app.run(debug=True)
