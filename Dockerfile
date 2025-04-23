FROM python:3.11

WORKDIR /app

# Install system dependencies for dlib
RUN apt-get update && apt-get install -y     build-essential     cmake     libboost-all-dev     && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:10000", "backend.app:app"]
