FROM python:3.6.0-alpine
LABEL maintainer "Tomek Wiszniewski <t.wiszniewski@gmail.com>"
  # Because MAINTAINER seems to be depracated 😬

WORKDIR /the-next-big-flask-thing/

COPY src/ /the-next-big-flask-thing/
COPY requirements.txt /the-next-big-flask-thing/

RUN ["pip", "install", "-r", "/the-next-big-flask-thing/requirements.txt"]
CMD ["python", "/the-next-big-flask-thing/src/app.py"]
