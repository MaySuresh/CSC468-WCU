FROM node:4-slim

RUN npm install redis@2

COPY templates/ /templates/
COPY app.py /
CMD ["node","/app.py"]
EXPOSE 80
