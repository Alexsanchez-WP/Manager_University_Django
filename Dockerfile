FROM python:3.8



RUN mkdir /code
WORKDIR /code

COPY . /code

RUN python -m pip install -r requirements.txt