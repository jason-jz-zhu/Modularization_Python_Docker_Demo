# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Install gcc & cron
RUN apt-get update && apt-get install gcc -y && apt-get clean

# Install the requirements
COPY requirements.txt /
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Set the working directory and install the adopt package
WORKDIR /demo
ADD . /demo
RUN pip install .

COPY crontab.yaml /etc/yacron.d/yacrontab.yaml

CMD /usr/local/bin/yacron