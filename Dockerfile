FROM python:3.10.5-slim

RUN useradd -ms /bin/bash myfituser

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements-dev.txt /tmp/requirements-dev.txt
RUN cd /tmp/ && pip install -r requirements-dev.txt

COPY --chown=myfituser:myfituser . /app

USER myfituser
