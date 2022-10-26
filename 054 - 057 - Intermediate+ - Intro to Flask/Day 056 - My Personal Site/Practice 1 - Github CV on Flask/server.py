from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")


if __name__ == "__main__":
    app.run(debug=True)