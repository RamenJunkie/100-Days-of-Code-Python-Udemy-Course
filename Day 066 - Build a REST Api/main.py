from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice
import json

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['JSON_SORT_KEYS'] = False

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
  cafes = Cafe.query.all()
  rand_cafe = choice(cafes)

#### BETTER Coupled with Line 28
  return jsonify(cafe=rand_cafe.to_dict())

@app.route("/all")
def get_all_cafe():
  all_cafes = [cafe.to_dict() for cafe in Cafe.query.all()]
  return jsonify(cafes = all_cafes)

@app.route("/search")
def search_cafe():
    loc = request.args['loc']
    search_cafes = [cafe.to_dict() for cafe in Cafe.query.filter_by(location=loc).all()]
    if len(search_cafes) == 0:
        return jsonify(error="Sorry, No cafes at this location.")

    return jsonify(cafes=search_cafes)

## HTTP POST - Create Record


## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)




#### FOR POSTERITY

#### ORIGINAL GET return
#   return jsonify(name = rand_cafe.name,
#   can_take_calls = rand_cafe.can_take_calls,
#   coffee_price = rand_cafe.coffee_price,
#   has_sockets = rand_cafe.has_sockets,
#   has_toilets = rand_cafe.has_toilet,
#   has_wifi = rand_cafe.has_wifi,
#   seats = rand_cafe.seats,
#   img_url = rand_cafe.img_url,
#   location = rand_cafe.location,
#   map_url = rand_cafe.map_url
# )