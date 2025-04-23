FROM python:3.11
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y cmake build-essential libboost-all-dev && pip install --upgrade pip && pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:10000 backend.app:app