from flask import Flask, render_template
import os

# This tells Flask to look inside backend/templates by default
app = Flask(__name__, template_folder="templates")

@app.route("/")
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
