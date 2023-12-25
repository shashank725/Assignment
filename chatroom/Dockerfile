# syntax=docker/dockerfile:1
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir --upgrade pip

WORKDIR /code
# COPY ./chatroom/requirements.txt /code/
COPY requirements.txt .
RUN pip install -r requirements.txt
# COPY . /code/
COPY . .