FROM python:3.8.1-slim

# set work directory
WORKDIR /app

# copy requirements file
COPY ./requirements.txt /app/requirements.txt

# install dependencies

RUN pip install -r /app/requirements.txt 

ADD . .

CMD uvicorn main:app --reload --workers 2 --host 0.0.0.0 --port 80
