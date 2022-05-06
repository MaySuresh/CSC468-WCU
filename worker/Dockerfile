# FROM python:alpine
# RUN pip install redis
# RUN pip install requests
# RUN pip install praw
# RUN pip install flask
# COPY app.py /
# CMD ["python", "app.py"]
# EXPOSE 80
#Create a ubuntu base image with python 3 installed.
FROM python:3.8-slim-buster

#Set the working directory
WORKDIR /usr/src/app

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN pip3 install -r requirements.txt

#Expose the required port
EXPOSE 3000

#Run the command
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]