FROM python:3.9.5-slim-buster
RUN pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN  pip install -r /tmp/requirements.txt
WORKDIR /bulba
ADD . /bulba