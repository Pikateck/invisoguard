FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY wheels/ /wheels/
RUN pip install --upgrade pip &&     pip install --no-cache-dir /wheels/dlib-19.24.0-cp311-cp311-manylinux_x86_64.whl &&     pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "backend.app:app"]
