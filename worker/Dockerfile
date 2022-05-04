FROM python:alpine
RUN pip install redis
RUN pip install requests
RUN pip install praw
RUN pip install flask
COPY app.py /
CMD ["python", "app.py"]
