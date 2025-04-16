
from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager
app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

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

@app.route('/trace_result')
def trace_result():
    return render_template('trace_result.html')

if __name__ == '__main__':
    app.run(debug=True)
