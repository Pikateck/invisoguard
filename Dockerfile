FROM python:3.11-slim

# System dependencies for dlib
RUN apt-get update && apt-get install -y     cmake     g++     make     build-essential     libgl1-mesa-glx     libgtk-3-dev     python3-dev     && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
