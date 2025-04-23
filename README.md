
# InvisoGuard – Phase 1: Production Ready

## 🎯 Core Feature: Reverse Video Identity Tracing with Biometric Cross-Match

This system identifies video uploaders by simulating:
- Device metadata parsing
- Face match score (simulated)
- Location trace and timestamp
- PDF generation of trace result

## ✅ Test Credentials
- **Email:** test@invisoguard.com
- **Password:** test123

## 🧪 Test Instructions
1. Run `python app.py`
2. Login with the test credentials.
3. Upload a video file.
4. View and download the PDF trace result.

## 📁 Folder Structure
- `/backend`: Flask logic + trace engine
- `/templates`: UI pages (HTML)
- `/static`: CSS, JS, assets

## 📦 Dependencies
Listed in `requirements.txt`. Use:
```bash
pip install -r requirements.txt
```

## 🚀 Deployment Ready
Use Render or any Docker host. Includes `Dockerfile` and `.render.yaml`.
