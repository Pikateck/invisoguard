# InvisoGuard

## Setup (Local)
1. Install Docker
2. Build and run the container:
   ```
   docker build -t invisoguard .
   docker run -p 5000:5000 invisoguard
   ```

## Deployment
- Frontend: Vercel (React build)
- Backend: Render (Docker deployment)

Includes SQLite, face recognition, and secure trace logic.

### To trigger a GitHub Actions build:
```bash
git commit --allow-empty -m "Trigger build"
git push origin main
```
