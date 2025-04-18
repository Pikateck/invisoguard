
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/trace")
def trace():
    return render_template("trace.html")

@app.route("/trace_result")
def trace_result():
    return render_template("trace_result.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/authority_dashboard")
def authority_dashboard():
    return render_template("authority_dashboard.html")

@app.route("/admin_panel")
def admin_panel():
    return render_template("admin_panel.html")

@app.route("/subscription")
def subscription():
    return render_template("subscription.html")

@app.route("/receipt")
def receipt():
    return render_template("receipt.html")

@app.route("/alert_trigger")
def alert_trigger():
    return render_template("alert_trigger.html")

@app.route("/forgot_password")
def forgot_password():
    return render_template("forgot_password.html")

@app.route("/profile_match")
def profile_match():
    return render_template("profile_match.html")

if __name__ == "__main__":
    app.run(debug=True)
