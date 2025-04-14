
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

ADMIN_USERNAME = "admin@invisoguard.com"
ADMIN_PASSWORD = "Test@1234"

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return "✅ Login successful. Welcome to InvisoGuard."
        return "❌ Invalid credentials. Try again."
    return render_template_string(open("frontend/index.html").read())

if __name__ == "__main__":
    app.run(debug=True)
