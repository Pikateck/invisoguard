# InvisoGuard Full Production Setup

## How to Run Locally
1. Create a virtual environment and activate it.
2. Run `pip install -r requirements.txt`
3. Run `python app.py`

## Deployment on Render
1. Upload all files to GitHub.
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `gunicorn app:app`
