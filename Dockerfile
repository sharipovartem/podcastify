# Use an official Python runtime as a parent image
FROM python:3.12.2-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
# Install git
RUN apk update && apk add git

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8088 available to the world outside this container
EXPOSE 8088

# Define environment variable
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
# Install ffmpeg for pydub
RUN apt-get update && apt-get install -y ffmpeg

# Run main.py when the container launches using Python
CMD ["python", "main.py"]
