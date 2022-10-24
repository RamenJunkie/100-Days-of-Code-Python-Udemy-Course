from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def embolden():
        text = function()
        return f"<b>{text}</b>"
    return embolden

def make_emphasis(function):
    def emphasise():
        text = function()
        return f"<em>{text}</em>"
    return emphasise

def make_underline(function):
    def underliner():
        text = function()
        return f"<u>{text}</u>"
    return underliner


@app.route('/')
def hello_world():
    return '<strong>Howdy, Motherfuckers.<strong>'
@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bai bai!"

if __name__ == "__main__":
    app.run()

