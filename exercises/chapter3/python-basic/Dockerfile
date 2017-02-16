#FROM <a chosen operating system image>
#MAINTAINER "<your name and username>"
FROM python:3.5

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY src/ /app/
#COPY <something else> <to some location inside the container>

#CMD <run the Python app in the foreground>
CMD python /app/app.py
