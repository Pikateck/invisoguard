
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace():
    video_url = request.form.get('video_url')
    result = {
        'video_url': video_url,
        'location': '[Mock GPS Coordinates]',
        'device_id': '[Mock Device ID]',
        'token_usage': 1
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
