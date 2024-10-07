FROM python:3.11-slim

WORKDIR /app
COPY ./book_catalog/requirements.txt .
COPY ./book_catalog/app .
RUN pip install -r ./requirements.txt
CMD uvicorn main:app --host 0.0.0.0 --port $PORT