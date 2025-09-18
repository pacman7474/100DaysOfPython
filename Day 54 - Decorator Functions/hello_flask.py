from flask import Flask
app = Flask(__name__)

def make_bold(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return (f"<b>{result}</b>")
    return wrapper

def make_emphasis(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return (f"<em>{result}</em>")
    return wrapper

def make_underline(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return (f"<u>{result}</u>")
    return wrapper

@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExejJxbTNzdmxsOHdhZ3MzY3F3dTQ0aHc1aXpxN2l3cXR2OHNjbmV2ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mcJohbfGPATW8/giphy.gif" width=200>'
            )


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye_world():
    return 'Bye!'



@app.route('/username/<name>/1')
def greet(name):
    return f"Hello, {name}"





if __name__ == "__main__":
    app.run(debug=True)