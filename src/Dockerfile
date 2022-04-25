# pull official base image
FROM python:3.10.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install pipenv curl \
    && pip install --upgrade pip setuptools wheel \
    && apt-get clean

# install dependencies
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --system --deploy


# copy project
COPY . /usr/src/app/

# Install Tailwind cli so there is no need for node.js
RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 \
    && chmod +x tailwindcss-linux-x64 \
    && mv tailwindcss-linux-x64 /usr/src/app/tailwindcss