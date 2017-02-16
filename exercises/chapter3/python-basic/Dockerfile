FROM python:3.5.3
MAINTAINER marbu

COPY src /
COPY requirements.txt /

RUN pip install -r /requirements.txt

CMD python /app.py

# To build:
# $ docker build -t marflask .
#
# To run:
# $ docker run -p 5000:5000 marflask
#
# Is running failing? troubleshoot:
# $ docker run -ti library/marflask bash
#
# To push:
# $ docker images
# $ docker tag [IMAGE_ID] marbu/marflask:latest
# $ docker push marbu/marflask
