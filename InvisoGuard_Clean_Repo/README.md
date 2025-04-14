
# InvisoGuard

## How to Run Locally
```bash
pip install -r requirements.txt
python backend/app.py
```

## Render Start Command
```
gunicorn backend.app:app --bind 0.0.0.0:$PORT
```
