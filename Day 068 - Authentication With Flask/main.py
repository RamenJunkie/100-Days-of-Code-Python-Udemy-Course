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
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=(["POST", "GET"]))
def register():
    if request.form.get("name"):
        new_user = User()
        new_user.name = str(request.form.get("name"))
        new_user.email = request.form.get("email")
        new_user.password = werkzeug.security.generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/secrets')

    return render_template("register.html")


@app.route('/login', methods=(["POST", "GET"]))
def login():
    if request.form.get("email"):
        check_user = User.query.filter_by(email = request.form.get("email")).all()
        if not check_user:
            return render_template("login.html")

        if werkzeug.security.check_password_hash(check_user[0].password, request.form.get("password")):
            print("Success!")
        else:
            print("Fail!")
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory(directory=app.static_folder, path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
