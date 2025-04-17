
from flask import Flask, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'secretkey'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = { 'admin': User('admin') }

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

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
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/trace")
@login_required
def trace():
    return render_template("trace.html")

@app.route("/payment")
@login_required
def payment():
    return render_template("payment.html")

if __name__ == "__main__":
    app.run(debug=True)
