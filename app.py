
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/trace')
def trace():
    return render_template("trace.html")

@app.route('/result')
def trace_result():
    return render_template("trace_result.html")
