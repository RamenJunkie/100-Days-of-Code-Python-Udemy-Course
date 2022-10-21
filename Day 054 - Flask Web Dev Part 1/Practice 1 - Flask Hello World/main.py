from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<strong>Howdy, Motherfuckers.<strong><br><br><img src="aurora_howdy.jpg" width="500">'

#
