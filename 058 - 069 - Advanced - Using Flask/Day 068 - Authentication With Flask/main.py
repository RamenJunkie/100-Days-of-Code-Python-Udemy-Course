import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = '6fce45vu88rte4buii'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

#Line below only required once, when creating DB. 
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=(["POST", "GET"]))
def register():
    if request.form.get("name"):
        check_user = User.query.filter_by(email = request.form.get("email")).first()
        if check_user:
            flash(u'Account already exists.', 'error')
            return render_template("login.html")
        else:
            new_user = User()
            new_user.name = str(request.form.get("name"))
            new_user.email = request.form.get("email")
            new_user.password = werkzeug.security.generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('secrets', name=new_user.name))

    return render_template("register.html")


@app.route('/login', methods=(["POST", "GET"]))
def login():
    if request.form.get("email"):
        check_user = User.query.filter_by(email = request.form.get("email")).first()
        if not check_user:
            flash(u'Account Not Found.', 'error')
            return render_template("login.html")

        if werkzeug.security.check_password_hash(check_user.password, request.form.get("password")):
            login_user(check_user)
            return redirect(url_for('secrets', name=check_user.name))
        else:
            flash(u'Incorrect Password.', 'error')
    return render_template("login.html")


@app.route('/secrets/<name>')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory=app.static_folder, path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
