
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

ADMIN_USERNAME = "admin@invisoguard.com"
ADMIN_PASSWORD = "Test@1234"

@app.route("/")
def home():
    return "InvisoGuard is running."

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form.get("username")
        p = request.form.get("password")
        if u == ADMIN_USERNAME and p == ADMIN_PASSWORD:
            return "✅ Login Successful."
        else:
            return "❌ Invalid credentials."
    return '''
        <form method="post">
            <input name="username" placeholder="Username" required><br>
            <input name="password" type="password" placeholder="Password" required><br>
            <button type="submit">Login</button>
        </form>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
