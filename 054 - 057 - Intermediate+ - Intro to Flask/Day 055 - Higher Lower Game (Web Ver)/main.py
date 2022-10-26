from flask import Flask
from random import randint, choice

app = Flask(__name__)

answer = randint(1, 20)



nope_gifs = ["https://media.giphy.com/media/l46CzBXeuj9AaV4fS/giphy.gif",
             "https://media.giphy.com/media/d1FL3ompUVeYavvi/giphy.gif",
             "https://media.giphy.com/media/3oEjHZFzgi0u3Lwozm/giphy.gif",
             "https://media.giphy.com/media/3o6gDQtfeqlhhINRq8/giphy.gif",
             "https://media.giphy.com/media/7E8JECFYErLj48u8s2/giphy-downsized-large.gif",
             "https://media.giphy.com/media/3gIIbKUMyPUgmw67I9/giphy.gif",
             "https://media.giphy.com/media/3o7bujBB0PzWWtfRS0/giphy.gif",
             "https://media.giphy.com/media/2djT3MwdZzl0lknXT4/giphy-downsized-large.gif",
             "https://media.giphy.com/media/cO8BQGfRKczD9BipO6/giphy-downsized-large.gif",
             "https://media.giphy.com/media/l3vR4DPpgHbpJbW6c/giphy.gif",
             "https://media.giphy.com/media/xT5LMwOY4Ob94sg1Da/giphy.gif",
             "https://media.giphy.com/media/xT5LMF4vKdsw49Ufmw/giphy.gif",]

choices = '<p style="text-align: center; font-size: 2em;">Choices'

for i in range(1,21):
    choices += f'  |  <a href="{str(i)}">{str(i)}</a>'

choices += "</p>"


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Howdy, Motherfuckers.</h1>' \
           '<h2 style="text-align: center">Welcome to the Number Guessing Game.</h2>' \
           '<img src="https://i.ytimg.com/vi/MOfVRxaYI_Y/maxresdefault.jpg" width=500 style="display: block;' \
           'margin-left: auto; margin-right: auto;">' \
           f'<p style="text-align: center">Make a Guess!</p>{choices}'


@app.route('/bye')
def bye():
    return "Bai bai!"


@app.route('/<int:number>')
def guess(number):
    if number < 1 or number > 20:
        return "Guess between 1 and 20"
    elif number == answer:
        return '<h1 style="text-align: center">You guessed it!.</h1><br><br>' \
               '<img src="https://media.giphy.com/media/5qFDlI2XyplPLnUZ1l/giphy.gif" width=500 style="display: block;' \
               'margin-left: auto; margin-right: auto;">'
    elif number < answer:
        image = choice(nope_gifs)
        return f'<h1 style="text-align: center">Higher!.</h1><br><br>' \
               f'<img src="{image}" width=500 style="display: block;' \
               f'margin-left: auto; margin-right: auto;">' \
               f'<p style="text-align: center">Make a Guess!</p>{choices}'
    else:
        image = choice(nope_gifs)
        return f'<h1 style="text-align: center">Lower!.</h1><br><br>' \
               f'<img src="{image}" width=500 style="display: block;' \
               f'margin-left: auto; margin-right: auto;">' \
               f'<p style="text-align: center">Make a Guess!</p>{choices}'


if __name__ == "__main__":
    app.run()
