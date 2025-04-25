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