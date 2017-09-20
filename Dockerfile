# Dockerfile to build resmount container image
# Based on Ubuntu 16.04 and python3

FROM ubuntu:16.04

MAINTAINER Kosy Anyanwu

RUN apt-get update && apt-get install -y python3

WORKDIR /app

ADD . /app

EXPOSE 5555

CMD ["python3", "server.py"]
