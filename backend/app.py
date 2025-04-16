from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace():
    # Placeholder logic
    return {
        "location": "Ghaziabad, India",
        "device_id": "Samsung-A53",
        "timestamp": "2025-04-06 14:32",
        "trace_id": "TRACE-58C2-XF91",
        "face_match": "Yes",
        "user": {
            "name": "Rohit Sharma",
            "phone": "+91-98123-45678",
            "email": "rohit123@gmail.com"
        }
    }
