
from flask import Flask, render_template, request, redirect, session, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
app = Flask(__name__)
app.secret_key = 'super-secret-key'

login_manager = LoginManager()
login_manager.init_app(app)

users = {'admin@invisoguard.com': {'password': 'admin123'}}

class User(UserMixin):
    def __init__(self, email): self.id = email

@login_manager.user_loader
def load_user(email): return User(email) if email in users else None

@app.route('/')
def home(): return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email, pw = request.form['email'], request.form['password']
        if email in users and users[email]['password'] == pw:
            login_user(User(email))
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
