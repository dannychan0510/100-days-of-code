from flask import Flask, render_template_string, request, redirect
import random


app = Flask(__name__)

def generate_number():
    return random.randint(0, 9)

answer = generate_number()

@app.route("/", methods=["GET", "POST"])
def guess_number():
    global answer
    if request.method == "POST":
        user_input = int(request.form["user_input"])
        return redirect(f"/{user_input}")
    
    # Only generate new number if coming from a correct guess (with play_again=1)
    if request.args.get('play_again') == '1':
        answer = generate_number()
        
    return render_template_string('''
        <h1>Guess a number between 1 and 9</h1>
        <form action="" method="post">
            <select name="user_input" required style="width: 200px;">
                <option value="" disabled selected>Select a number</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
            </select>
            <input type="submit" value="Submit">
        </form>
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Guess a number gif">
    ''')

@app.route("/<int:user_input>")
def check_guess(user_input):
    if user_input == answer:
        return f'''
            <h1>Correct!</h1><a href='/?play_again=1'><button>Play Again</button></a>
            <br><br>
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='Play Again gif'>"
            '''
    elif user_input > answer:
        return '''
            <h1>Too high! Try again.</h1>
            <a href="/"> <button>Try Again</button> </a>
            <br><br>
            <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Too high gif">
        '''
    else:
        return '''
            <h1>Too low! Try again.</h1>
            <a href="/"> <button>Try Again</button> </a>
            <br><br>
            <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Too low gif">
        '''

if __name__ == "__main__":
    app.run(debug=True)
