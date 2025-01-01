from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_underline(function):   
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
@make_bold
@make_underline
def hello_world():
    return "Hello, World!"

@app.route("/bye")
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)