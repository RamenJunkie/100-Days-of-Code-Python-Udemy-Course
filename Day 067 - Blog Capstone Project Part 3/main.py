from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime
import bleach


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBssdas    A6O6donzWlSgfdaihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## strips invalid tags/attributes by hank-ux
def strip_invalid_html(content):
    allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul']
    allowed_attrs = {
        'a': ['href', 'target', 'title'],
        'img': ['src', 'alt', 'width', 'height'],
    }
    cleaned = bleach.clean(content,
                           tags=allowed_tags,
                           attributes=allowed_attrs,
                           strip=True)

    return cleaned

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    id=index
    requested_post = BlogPost.query.get(id)
    return render_template("post.html", post=requested_post)


@app.route("/new_post/", methods=['GET', 'POST'])
def new_post(post_id=0):
    header="New Post"
    form=CreatePostForm()

    if form.validate_on_submit():
        new_blog = BlogPost()
        new_blog.title = form.title.data
        new_blog.subtitle = form.subtitle.data
        new_blog.author = form.author.data
        new_blog.img_url = form.img_url.data
        new_blog.body = strip_invalid_html(form.body.data)
        new_blog.date = datetime.now().strftime("%A %d, %Y")
        db.session.add(new_blog)
        db.session.commit()
        return redirect('/')

    return render_template("make-post.html", form=form, header=header)

@app.route("/editor/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    header = "Edit Post"
    form = CreatePostForm()
    id = post_id
    requested_post = BlogPost.query.get(id)

    if form.validate_on_submit():
        requested_post.title = form.title.data
        requested_post.subtitle = form.subtitle.data
        requested_post.author = form.author.data
        requested_post.img_url = form.img_url.data
        requested_post.body = strip_invalid_html(form.body.data)
        db.session.commit()

        return redirect('/')

    form.title.data = requested_post.title
    form.subtitle.data = requested_post.subtitle
    form.author.data = requested_post.author
    form.body.data = requested_post.body
    form.img_url.data = requested_post.img_url

    return render_template("make-post.html", form=form, header=header)

@app.route("/delete/<post_id>")
def delete(post_id):
    ### MAKE THIS A CONFIRM PAGE OR SOMETHING LATER.
    requested_post = db.session.query(BlogPost).get(post_id)
    if not requested_post:
        return redirect('/')
    db.session.delete(requested_post)
    db.session.commit()
    return redirect('/')

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)