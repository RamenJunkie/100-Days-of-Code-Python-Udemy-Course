from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<strong>Howdy, Motherfuckers.<strong>'
@app.route('/bye')
def bye():
    return "Bai bai!"

if __name__ == "__main__":
    app.run()

