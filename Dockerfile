FROM python:3.11-slim

COPY ./src /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python3 /app/src/app.py

EXPOSE 5000
