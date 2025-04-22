FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential cmake libopenblas-dev \
    liblapack-dev libx11-dev libgtk-3-dev \
    libboost-all-dev wget unzip ffmpeg \
    && apt-get clean

RUN pip install --upgrade pip
RUN pip install numpy==1.24.4

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
