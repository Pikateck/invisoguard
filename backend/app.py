from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace():
    video_url = request.form.get('video_url')
    # This is where live trace logic would be placed
    details = {
        'location': 'London, England (51.5085, -0.1257)',
        'device': 'iPhone 14 Pro',
        'uploader': 'Jack Turner'
    }
    return render_template('trace.html', video_url=video_url, details=details)
