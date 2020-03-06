FROM ubuntu:16.04

MAINTAINER Your Name "Edwin Fung eedwinfung@gmail.com"

FROM python:3.6.10-slim-buster

WORKDIR /app

ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD . /app

ENTRYPOINT [ "python" ]

CMD [ "application.py" ]