FROM node:4-slim

RUN npm install redis@2

FROM iron/python:2.7
WORKDIR /app
ADD . /app
RUN set -xe \
    && apt-get update \
    && apt-get install python-pip
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

COPY templates/ /templates/
COPY web.py /
CMD ["node","/web.py"]
EXPOSE 80
