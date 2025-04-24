FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y cmake g++ make
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "backend.app:app"]
