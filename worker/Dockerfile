FROM python:alpine
RUN pip install redis
RUN pip install requests
COPY bot.py /
CMD ["python", "bot.py"]
