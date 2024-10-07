FROM python:3.11-slim

WORKDIR /app
COPY ./inventory_management/requirements.txt .
COPY ./inventory_management/app .
RUN pip install -r ./requirements.txt
CMD uvicorn main:app --host 0.0.0.0 --port $PORT