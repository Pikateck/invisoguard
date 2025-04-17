
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'supersecretkey'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return None  # Placeholder for real user loading logic

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/trace")
def trace():
    return render_template("trace.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")

if __name__ == "__main__":
    app.run(debug=True)
