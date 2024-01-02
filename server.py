from flask import Flask
import random
app = Flask(__name__)
random_number = random.randint(0,9)

@app.route('/')
def render_home_page():
    return ('<h1 style="text-align: center"> Guess the number </h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')



@app.route('/<number>')
def check_the_number(number):
    if int(number) == random_number:
        return ('<h1 style="text-align: center"> Yay! You guessed correctly </h1>'
                '<img src="https://media.giphy.com/media/26tOZ42Mg6pbTUPHW/giphy.gif">')
    elif int(number) > random_number:
        return ('<h1 style="text-align: center"> Oops! That\'s too high!</h1>'
                '<img src="https://media.giphy.com/media/SyemapFxj7TiM/giphy.gif">')
    else:
        return ('<h1 style="text-align: center"> Oops! That\'s too low! </h1>'
                '<img src="https://media.giphy.com/media/aOthufs9X1rhMZYQL9/giphy.gif">')


if __name__ == '__main__':
    app.run(debug=True)