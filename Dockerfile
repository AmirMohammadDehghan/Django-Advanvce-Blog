# Pull base image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# copy project
COPY ./core /app

# cmd commands
# CMD [ "python3" , "manage.py", "runserver", "0.0.0.0:8000"]
