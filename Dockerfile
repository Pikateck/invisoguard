FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential cmake \
    libgtk-3-dev libboost-all-dev \
    libopenmpi-dev libglib2.0-0 libsm6 libxext6 libxrender-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
