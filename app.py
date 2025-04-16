
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace():
    video_url = request.form.get('video_url')
    # Simulate processing logic here
    return render_template('trace.html', video_url=video_url)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/subscription')
def subscription():
    return render_template('subscription.html')

if __name__ == '__main__':
    app.run(debug=True)
