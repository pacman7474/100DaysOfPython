from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def higher_lower():
    return ('<h1 style="text-align: center">Guess a number between 0 and 9</h1>'
            '<img style="margin-left:auto;margin-right:auto;display:block" '
            'src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjdlanhxemlyMmM5NGM1YXNtMTN3bXVueHh3c3FmbTl4cnVmdWhnMyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Cij37iSqbvzEpLgZmN/giphy.gif">'
            )


@app.route('/<int:number>')
def num_guess(number):
    result = ""
    if number < my_num:
        result = result = '<h1 style="text-align: center;color: purple">Too low, try again</h1>' \
            '<img style="margin-left:auto;margin-right:auto;display:block" ' \
            'src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGhtZzB1YWd4eno0bHd1cnZyemptZGU1a2F1NHllOXk3NW50MDZoMCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/WfJyRpgey7o6HQi4Kk/giphy.gif">'
    elif number > my_num:
        result = '<h1 style="text-align: center;color: red">Too high, try again</h1>' \
            '<img style="margin-left:auto;margin-right:auto;display:block" ' \
            'src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcG96bDRqMm5yazltYXRxYmk1ZWd1Z2JldHd4bHZka3pmZW52bzF2dSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/19gjcpEUzbIRJ5OpcQ/giphy.gif">'
    else:
        result = '<h1 style="text-align: center">Just Right</h1>' \
            '<img style="margin-left:auto;margin-right:auto;display:block" ' \
            'src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2I2enBsNnIzNzJiaW02MGlrYXBkbnRkdHB0amNseTRpZmY2bmY4cSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/xsBurJCrgGLwMfpawF/giphy.gif">'

    return result


my_num = random.randint(0,9)

if __name__ == "__main__":
    app.run(debug=True)