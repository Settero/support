FROM python:3.12-slim

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY app.py .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
