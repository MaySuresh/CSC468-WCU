FROM node:4-slim

RUN npm install redis@2
apt install python3-flask

COPY templates/ /templates/
COPY web.py /
CMD ["node","/web.py"]
EXPOSE 80
