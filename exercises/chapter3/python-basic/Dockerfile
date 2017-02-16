FROM python:3.6-alpine

MAINTAINER Carlos Mateo - carlosmateo

# Add requirements.
COPY requirements.txt ./

# Copy sample app
COPY src/ /

EXPOSE 5000

RUN pip install -r ./requirements.txt


CMD export FLASK_APP=/app.py; flask run --host=0.0.0.0