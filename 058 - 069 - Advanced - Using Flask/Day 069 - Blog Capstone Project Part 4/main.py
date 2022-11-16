from functools import wraps

import bleach
import werkzeug
from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from forms import CreatePostForm
from flask_gravatar import Gravatar
from flask_wtf import FlaskForm

def validate_pass(form, field):
    if len(field.data) < 8:
        raise ValidationError(u'Password must be 8 characters or longer.')

def validate_email(form, field):
    if "@" not in field.data or field.data[-4] != ".":
        raise ValidationError(u'Invalid Email Address.')

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

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBAjhuigjk6O6donzW99877BXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

gravatar = Gravatar(app,
                    size=250,
                    rating='r',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

##CONFIGURE TABLES

class User(UserMixin, db.Model):
    __tablename__ = "blog_users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="author")

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("blog_users.id"))
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="posts")

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("blog_users.id"))
    author = relationship("User", back_populates="comments")
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    posts = relationship("BlogPost", back_populates="comments")

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), validate_email])
    password = PasswordField('Password', validators=[DataRequired(), validate_pass])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), validate_email])
    password = PasswordField('Password', validators=[DataRequired(), validate_pass])
    submit = SubmitField('Login')

class CommentForm(FlaskForm):
    body = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField('Submit Comment')



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            if current_user.id == 1:
                return f(*args, **kwargs)
        return abort(403, description="NOT ALLOWED")
    return decorated_function


@app.route('/')
def get_all_posts():
    db.create_all()
    if current_user.is_authenticated:
        cur_id = current_user.id
    else:
        cur_id = -1
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts, uuid=cur_id)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.errorhandler(403)
def not_allowed(e):
    # note that we set the 404 status explicitly
    return render_template('403.html'), 403


@app.route('/register', methods=(["POST", "GET"]))
def register():
    form = RegisterForm()
    if request.form.get("name"):
        check_user = User.query.filter_by(email = request.form.get("email")).first()
        if check_user:
            flash(u'Account already exists.', 'error')
            return redirect(url_for('login', form=LoginForm()))
        else:
            new_user = User()
            new_user.name = str(request.form.get("name"))
            new_user.email = request.form.get("email")
            new_user.password = werkzeug.security.generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('get_all_posts'))

    return render_template("register.html", form=form)


@app.route('/login', methods=(["POST", "GET"]))
def login():
    form = LoginForm()
    if request.form.get("email"):
        check_user = User.query.filter_by(email = request.form.get("email")).first()
        if not check_user:
            flash(u'Account Not Found.', 'error')
            return render_template("login.html", form=form)

        if werkzeug.security.check_password_hash(check_user.password, request.form.get("password")):
            login_user(check_user)
            return redirect(url_for('get_all_posts'))
        else:
            flash(u'Incorrect Password.', 'error')
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=(["POST", "GET"]))
def show_post(post_id):
    if current_user.is_authenticated:
        cur_id = current_user.id
    else:
        cur_id = -1
    requested_post = BlogPost.query.get(post_id)

    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(
            body=strip_invalid_html(form.body.data),
            author=current_user,
            posts = requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))

    print(requested_post.comments)
    return render_template("post.html", post=requested_post, uuid=cur_id, form=form)





@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/new-post", methods=(["POST", "GET"]))
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


##author = current_user.name,
## author=User.query.filter_by(id = post.author_id),


@app.route("/edit-post/<int:post_id>", methods=(["POST", "GET"]))
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body,
    )

    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = post.author
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
