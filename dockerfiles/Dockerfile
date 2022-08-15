FROM python:3.8-slim-buster
MAINTAINER Teranteks

EXPOSE 5000

RUN mkdir /app
WORKDIR /app

COPY ./main.py /app/app.py
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

CMD [ "python3", "./app.py"]
