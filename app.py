from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

game_data = {
    "secret": None,
    "attempts": 0,
    "lower": 1,
    "upper": 100
}

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""

    if request.method == 'POST':
        # Difficulty selection
        if 'difficulty' in request.form:
            level = request.form['difficulty']

            if level == 'easy':
                game_data['upper'] = 50
            elif level == 'medium':
                game_data['upper'] = 100
            elif level == 'hard':
                game_data['upper'] = 500

            game_data['secret'] = random.randint(
                game_data['lower'],
                game_data['upper']
            )
            game_data['attempts'] = 0
            return redirect(url_for('index'))

        # Guess submission
        try:
            guess = int(request.form.get('guess'))
            game_data['attempts'] += 1

            if guess == game_data['secret']:
                return redirect(url_for('win'))
            elif guess < game_data['secret']:
                message = "🔼 Higher!"
            else:
                message = "🔽 Lower!"
        except:
            message = "❌ Enter a valid number."

    return render_template(
        'index.html',
        message=message,
        attempts=game_data['attempts'],
        lower=game_data['lower'],
        upper=game_data['upper'],
        started=game_data['secret'] is not None
    )

@app.route('/win')
def win():
    return render_template(
        'win.html',
        secret=game_data['secret'],
        attempts=game_data['attempts']
    )

@app.route('/reset')
def reset():
    game_data['secret'] = None
    game_data['attempts'] = 0
    return redirect(url_for('index'))

if __name__ == "__main__": 
    app.run(debug=True)