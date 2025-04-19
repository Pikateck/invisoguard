
from flask import Flask, render_template
app = Flask(__name__)

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
    return render_template('trace.html')

@app.route('/trace/result')
def trace_result():
    return render_template('trace_result.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/authority')
def authority():
    return render_template('authority.html')

@app.route('/emergency')
def emergency():
    return render_template('emergency.html')

@app.route('/subscription')
def subscription():
    return render_template('subscription.html')

@app.route('/receipt')
def receipt():
    return render_template('receipt.html')

if __name__ == "__main__":
    app.run(debug=True)
