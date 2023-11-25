FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN mkdir /service
WORKDIR /service

RUN pip install --upgrade pip
COPY  ../requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .