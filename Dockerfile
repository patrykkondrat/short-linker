FROM python:3.10-slim

WORKDIR /short_linker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
CMD uvicorn --host 0.0.0.0 --port 3000 --reload main:app
