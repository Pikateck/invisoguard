
from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/", methods=["GET", "POST"])
def index():
    trace_data = None
    if request.method == "POST":
        video_url = request.form.get("video_url")
        trace_data = {
            "video_url": video_url,
            "location": "London, England (51.5085, -0.1257)",
            "device": "iPhone 14 Pro",
            "uploader": "Jack Turner"
        }
    return render_template("index.html", trace_data=trace_data)

if __name__ == "__main__":
    app.run(debug=True)
