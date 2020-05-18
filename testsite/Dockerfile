FROM python:3.7-alpine
MAINTAINER SimpleGuide

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app

ADD . /app/

RUN adduser -D dockuser
USER dockuser