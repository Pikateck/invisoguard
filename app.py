
from flask import Flask, render_template
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app) 

# Dummy User class (replace this with your actual User model)
class User:
    def __init__(self, id):
        self.id = id
        self.name = f"user{id}"
        self.email = f"user{id}@example.com"

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

# Required by Flask-Login to load user from session
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/trace')
def trace():
    return render_template('trace.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

if __name__ == '__main__':
    app.run(debug=True)
