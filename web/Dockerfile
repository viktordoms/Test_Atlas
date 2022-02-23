FROM python:3.9.5-slim-buster

WORKDIR /application

ENV PYTHONUNBUFFERED 1

RUN pip install flask

COPY ./requirements.txt /application/requirements.txt

RUN  pip install -r requirements.txt

COPY ./wait-for-it.sh /application/wait-for-it.sh

CMD ./wait-for-it.sh db:5432 -- python3 app.py

