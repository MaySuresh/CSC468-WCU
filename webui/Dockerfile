FROM node:4-slim

RUN npm install redis@2
export FLASK_APP=web.py
flask run

COPY templates/ /templates/
COPY web.py /
CMD ["node","/web.py"]
EXPOSE 80
