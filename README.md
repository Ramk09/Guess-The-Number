# 🎯 Number Guessing Game

A simple interactive **Number Guessing Game** built with **Python and Flask**.

The player selects a difficulty level, receives a randomly generated number within the selected range, and keeps guessing until the correct number is found.

## ✨ Features

- 🎚️ Three difficulty levels
- 🟢 Easy: numbers from 1 to 50
- 🟡 Medium: numbers from 1 to 100
- 🔴 Hard: numbers from 1 to 500
- 🎯 Random number generation
- 🔼 Higher / 🔽 Lower hints
- 🔢 Attempt counter
- ❌ Input validation for invalid numbers
- 🎉 Dedicated winning page
- 🔄 Play Again / reset option
- 🌐 Flask-based web interface

## 🛠️ Tech Stack

- Python
- Flask
- HTML
- CSS

## 📂 Project Structure

```text
number-guessing-game/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── win.html
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Ramk09/number-guessing-game.git
cd number-guessing-game
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open it in your browser

```text
http://127.0.0.1:5000/
```

## 🎮 How to Play

1. Choose **Easy**, **Medium**, or **Hard**.
2. The application generates a random number within the selected range.
3. Enter your guess.
4. The game tells you whether to guess **Higher** or **Lower**.
5. Continue until you find the correct number.
6. View your attempt count on the winning page.
7. Click **Play Again** to start a new game.

## 📌 What I Practiced

This project helped me practice:

- Python programming
- Flask routing
- Handling GET and POST requests
- HTML forms
- Jinja2 template rendering
- Random number generation
- User input validation
- Basic game logic
- Connecting frontend and backend

## 🔮 Future Improvements

- Add a maximum-attempt system
- Add a score based on attempts
- Store player scores
- Add a leaderboard
- Improve responsive UI
- Use Flask sessions for separate player game states

## 👨‍💻 Author

Kurra Venkata Siva Rama Krishna
Artificial Intelligence And Machine Learning

GitHub: https://github.com/Ramk09
