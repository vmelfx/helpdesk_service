FROM python:3.10.7-slim

ENV PYTHONBUGGERD=1

WORKDIR /app/


RUN apt-get update \
    && apt-get install -y build-essential \
    libcurl4-openssl-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip pipenv setuptools

COPY Pipfile Pipfile.lock ./

RUN pipenv sync --system --dev

COPY ./ ./