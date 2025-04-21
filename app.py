from flask import Flask, render_template
app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/trace')
def trace():
    return render_template('trace_input.html')

@app.route('/trace_result')
def trace_result():
    return render_template('trace_result.html')

@app.route('/face_match')
def face_match():
    return render_template('face_match.html')

@app.route('/emergency_alert')
def emergency_alert():
    return render_template('emergency_alert.html')

@app.route('/receipt')
def receipt():
    return render_template('receipt.html')

@app.route('/token_purchase')
def token_purchase():
    return render_template('token_purchase.html')

@app.route('/trigger_details')
def trigger_details():
    return render_template('trigger_details.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/authority_dashboard')
def authority_dashboard():
    return render_template('authority_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
