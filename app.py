from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/trace')
def trace():
    return render_template('trace.html')

@app.route('/trace-result')
def trace_result():
    return render_template('trace_result.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/emergency')
def emergency():
    return render_template('emergency.html')

@app.route('/receipt')
def receipt():
    return render_template('receipt.html')

@app.route('/token-voucher')
def token_voucher():
    return render_template('token_voucher.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/full-profile')
def full_profile():
    return render_template('full_profile.html')

@app.route('/authority-dashboard')
def authority_dashboard():
    return render_template('authority_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
