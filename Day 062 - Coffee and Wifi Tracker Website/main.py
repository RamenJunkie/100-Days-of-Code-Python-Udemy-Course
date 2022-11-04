from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

times = ('1 AM', '2 AM', '3 AM', '4 AM', '5 AM', '6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM',  '3 PM',  '4 PM',  '5 PM',  '6 PM',  '7 PM',  '8 PM',  '9 PM',  '10 PM',  '11 PM',  '12 AM', )

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    maps_url = URLField('Maps URL', validators=[DataRequired()])
    open_time = SelectField('Open Time', choices=[('1 AM'), ('2 AM'), ('3 AM'), ('4 AM'), ('5 AM'), ('6 AM'), ('7 AM'), ('8 AM'), ('9 AM'), ('10 AM'), ('11 AM'), ('12 PM'), ('1 PM'), ('2 PM'), ( '3 PM'), ( '4 PM'), ( '5 PM'), ( '6 PM'), ( '7 PM'), ( '8 PM'), ( '9 PM'), ( '10 PM'), ( '11 PM'), ( '12 AM')], validators=[DataRequired()])
    clos_time = SelectField('Closing Time', choices=[('1 AM'), ('2 AM'), ('3 AM'), ('4 AM'), ('5 AM'), ('6 AM'), ('7 AM'), ('8 AM'), ('9 AM'), ('10 AM'), ('11 AM'), ('12 PM'), ('1 PM'), ('2 PM'), ( '3 PM'), ( '4 PM'), ( '5 PM'), ( '6 PM'), ( '7 PM'), ( '8 PM'), ( '9 PM'), ( '10 PM'), ( '11 PM'), ( '12 AM')], validators=[DataRequired()])
    coff_qual = SelectField('Coffee Quality', choices=[('✘'),('☕'),('☕☕'),('☕☕☕'),('☕☕☕☕'),('☕☕☕☕☕')], validators=[DataRequired()])
    wifi_qual = SelectField('Wifi Quality', choices=[('✘'),('💪'),('💪💪'),('💪💪💪'),('💪💪💪💪'),('💪💪💪💪💪')], validators=[DataRequired()])
    powr_qual = SelectField('Power Outlets', choices=[('✘'),('🔌'),('🔌🔌'),('🔌🔌🔌'),('🔌🔌🔌🔌'),('🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    if form.validate_on_submit():
        new_cafe = f"\n{form.cafe.data},{form.maps_url.data} ,{form.open_time.data},{form.clos_time.data},{form.clos_time.data},{form.coff_qual.data},{form.powr_qual.data}"
        print(new_cafe)
        with open('cafe-data.csv',newline='', mode="a", encoding="utf8") as csv_file:
            csv_file.write(new_cafe)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
