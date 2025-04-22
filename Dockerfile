
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt requirements.txt

# Install necessary system dependencies
RUN apt-get update &&     apt-get install -y build-essential cmake curl libgl1-mesa-glx libglib2.0-0 &&     pip install --upgrade pip &&     pip install -r requirements.txt

COPY . .
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
