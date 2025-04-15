
from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/', methods=['GET', 'POST'])
def home():
    video_url = None
    if request.method == 'POST':
        video_url = request.form.get('video_url')
    return render_template('index.html', video_url=video_url)
