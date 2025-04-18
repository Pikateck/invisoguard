# Flask app entry point placeholder
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'InvisoGuard Running'

if __name__ == '__main__':
    app.run(debug=True)
