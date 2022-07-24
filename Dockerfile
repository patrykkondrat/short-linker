FROM python:3.10-slim

WORKDIR /short-linker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
CMD uvicorn main:app --reload