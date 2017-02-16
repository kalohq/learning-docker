FROM ubuntu:16.04
MAINTAINER Jeremiah Boyle "jeremiah.boyle@gmail.com"

WORKDIR /app

RUN apt-get update && apt-get install -yq python3 python3-pip

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY src /app

CMD [ "python3", "app.py" ]
