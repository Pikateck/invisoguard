from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/trace', methods=['GET', 'POST'])
def trace():
    return render_template('trace.html')

if __name__ == '__main__':
    app.run(debug=True)
