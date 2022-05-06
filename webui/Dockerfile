FROM node:4-slim
FROM python:alpine
RUN npm install redis@2

FROM alpine/python
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
