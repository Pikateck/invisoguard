# InvisoGuard Deployment (Render-Ready)

## ✅ Included:
- Precompiled dummy `dlib` wheel (replace with real one during deployment)
- Updated Dockerfile using: `pip install --no-cache-dir wheels/dlib-*.whl`
- All UI templates + static branding
- Flask backend with placeholder logic
- `sample_video.mp4` for simulation

## 🔐 Demo Credentials:
- **Username**: demo@invisoguard.com
- **Password**: demo1234

## 🚀 Deploying on Render:
1. Connect GitHub repo
2. Use included `.render.yaml`
3. All dependencies will be installed using Docker

> ⚠️ Replace dummy wheel in `/wheels/` with the real dlib .whl before production launch
