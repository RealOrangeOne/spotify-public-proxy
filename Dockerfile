FROM python:3.11-slim

COPY ./requirements.txt /app/

WORKDIR /app

RUN pip install --no-cache -r requirements.txt

COPY ./src /app/src

CMD python3 /app/src/app.py

EXPOSE 5000
