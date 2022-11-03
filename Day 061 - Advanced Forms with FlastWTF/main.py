from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import Form, StringField, PasswordField, Label, SubmitField, ValidationError
from flask_bootstrap import Bootstrap

valid_email = "admin@email.com"
valid_pass = "12345678"

def validate_pass(form, field):
    if len(field.data) < 8:
        raise ValidationError(u'Password must be 8 characters or longer.')

def validate_email(form, field):
    if "@" not in field.data or field.data[-4] != ".":
        raise ValidationError(u'Invalid Email Address.')

class MyForm(FlaskForm):
    name = StringField('Email Address', validators=[DataRequired(), validate_email])
    password = PasswordField('Password', validators=[DataRequired(), validate_pass])
    submit = SubmitField("Log In")

app = Flask(__name__)
app.secret_key = "jdfhsd733jd93lsnnq"
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = MyForm(meta={'csrf': True})
    if login_form.validate_on_submit():
        if login_form.name.data == valid_email and login_form.password.data == valid_pass:
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)