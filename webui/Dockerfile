FROM node:4-slim

RUN npm install redis@2
RUN pip install flask

COPY templates/ /templates/
COPY web.py /
CMD ["node","/web.py"]
EXPOSE 80
