from python:alpine3.19

workdir /app

copy main.py .

copy requirements.txt .

run pip install -r requirements.txt

cmd ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]