
from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace():
    data = request.get_json()
    url = data.get('video_url')

    # Simulated real trace logic
    response = {
        "location": "Bandra Station Tracks, Mumbai",
        "gps": "19.055, 72.8405",
        "device": "Samsung Galaxy S22 Ultra",
        "serial": "0943XXXX",
        "timestamp": "Apr 5, 2024 11:14 AM",
        "uploader": "Rahul Gupta",
        "social_handle": "@rahul.g",
        "face_match": "98%",
        "street_view": "https://www.google.com/maps/@19.055,72.8405,3a,75y,90t/data=!3m6!1e1!3m4!1s0x0:0x0!7i13312!8i6656"
    }
    return jsonify(response)
