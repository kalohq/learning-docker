FROM python:3.6.0-alpine
LABEL maintainer "Tomek Wiszniewski <t.wiszniewski@gmail.com>"
  # Because MAINTAINER seems to be depracated 😬

COPY src /the-next-big-flask-thing/src
COPY requirements.txt /the-next-big-flask-thing/

WORKDIR /the-next-big-flask-thing/

RUN ["pip", "install", "-r", "requirements.txt"]
CMD ["python", "src/app.py"]
