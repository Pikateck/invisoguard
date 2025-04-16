from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace():
    return jsonify({
        "location": "Ghaziabad, India",
        "device_id": "Samsung-G998B",
        "timestamp": str(datetime.datetime.now()),
        "face_match": "Yes (placeholder)",
        "trace_id": "TRACE-1A2B-3C4D",
        "token_used": 1,
        "user": {
            "name": "Rohit Sharma",
            "phone": "+91-98123-45678",
            "email": "rohit123@gmail.com"
        }
    })

@app.route('/admin/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/download-report')
def download_report():
    return "PDF download logic placeholder"

if __name__ == "__main__":
    app.run(debug=True)
