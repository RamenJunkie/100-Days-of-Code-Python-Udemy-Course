from flask import Flask
from flask import render_template
app = Flask(__name__)
from random import randint
import datetime
import requests

name = "Josh"

gender_api = "https://api.genderize.io/?name="
age_api = "https://api.agify.io/?name="

posts_api = "https://api.npoint.io/b1c641f654ac32a59f9c"

def get_posts():
    data = requests.get(posts_api)
    return data.json()

def erize(url, name):
    data = requests.get(url+name)
    data.raise_for_status()
    dump = data.json()
    try:
        return dump["gender"]
    except:
        return dump["age"]


@app.route("/")
def home():
    year = datetime.datetime.now().year
    random = randint(1,10)

    title = "Howdy, Motherfuckers!"
    return render_template("index.html", num = random, title = title, year = year)

@app.route("/guess/<string:name>")
def guesser(name):

    gender = erize(gender_api, name)
    age = erize(age_api, name)
    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route("/blog/<number>")
def getblog(number):
    print(number)
    posts = get_posts()
    return render_template("blog.html", posts = posts)

if __name__ == "__main__":
    app.run(debug=True)