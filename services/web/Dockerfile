FROM python:3.8.1-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requeriments.txt /usr/src/app/requeriments.txt
RUN pip install -r requeriments.txt

COPY . /usr/src/app/
