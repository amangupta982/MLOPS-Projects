# Basic Calculator App

A simple calculator web application built with Python (Flask) and HTML/CSS. 
This project is configured to run in Docker.

## Docker Commands 
docker ps                                   # See a list of all running containers
docker ps -a                                # See a list of all containers, even the ones not running
docker rm <hash>                            # Remove the specified container from this machine
docker rm $(docker ps -a -q)                # Remove all containers from this machine
docker images -a                            # Show all images on this machine
docker rmi <imagename>                      # Remove the specified image from this machine
docker rmi $(docker images -q)              # Remove all images from this machine


## How to run locally
1. Install requirements: `pip install -r requirements.txt`
2. Run app: `python app.py`

## How to run with Docker
1. Build image: `docker build -t basic-calculator .`
2. Run container: `docker run -p 8081:8080 basic-calculator`

## Push to Docker Hub:
1. docker login
2. docker tag basic-calculator aman98292/basic-calculator
3. docker push aman98292/basic-calculator