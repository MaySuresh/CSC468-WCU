FROM node:4-slim
RUN npm install redis@2

FROM ubuntu

RUN apt-get update && apt-get -y install python3 python3-pip
RUN apt-get -y upgrade 

RUN pip3 install flask
RUN pip3 install flask-redis

COPY templates/ /templates/
COPY app.py /
CMD ["node","/web.py"]
EXPOSE 80
