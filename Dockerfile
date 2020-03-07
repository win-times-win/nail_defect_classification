FROM ubuntu:16.04

MAINTAINER Your Name "Edwin Fung eedwinfung@gmail.com"

FROM tensorflow/tensorflow:2.1.0-py3

WORKDIR /app

ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD . /app

ENTRYPOINT [ "python" ]

CMD [ "application.py" ]