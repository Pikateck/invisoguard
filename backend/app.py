
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    trace_data = None
    if request.method == "POST":
        video_url = request.form.get("video_url")
        trace_data = {
            "video_url": video_url,
            "location": "Bandra Station Tracks, Mumbai",
            "device": "Samsung Galaxy S22 Ultra",
            "serial": "0943XXXX",
            "recorder": "Rahul Gupta",
            "timestamp": "Apr 5, 2024 11:14 AM"
        }
    return render_template("index.html", trace_data=trace_data)

if __name__ == "__main__":
    app.run(debug=True)
