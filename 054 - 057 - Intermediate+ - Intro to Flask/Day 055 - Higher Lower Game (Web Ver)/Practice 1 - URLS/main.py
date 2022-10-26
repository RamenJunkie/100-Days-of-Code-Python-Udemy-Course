from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Howdy, Motherfuckers.</h1><br><br>' \
           '<img src="https://i.ytimg.com/vi/MOfVRxaYI_Y/maxresdefault.jpg" width=500 style="display: block;' \
           'margin-left: auto; margin-right: auto;">'

@app.route('/bye')
def bye():
    return "Bai bai!"

## Add Variables to URL with <>
@app.route('/<path:name>/<int:age>')
def name(name, age):
    return f"<h1>Hello {name}</h1>Age: {age}."
## Converters
## string default,
## path, for slashes
## int

if __name__ == "__main__":
    app.run(debug=True)


### Debugger to save and reload without stop and restart server
