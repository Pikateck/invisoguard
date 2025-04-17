
from flask import Flask, render_template
from flask_login import LoginManager, current_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

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

@app.route("/subscription")
def subscription():
    return render_template("subscription.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@login_manager.user_loader
def load_user(user_id):
    return None  # Dummy loader for now
