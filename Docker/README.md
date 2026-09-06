# Basic Calculator App

A simple calculator web application built with Python (Flask) and HTML/CSS. 
This project is configured to run in Docker.

## How to run locally
1. Install requirements: `pip install -r requirements.txt`
2. Run app: `python app.py`

## How to run with Docker
1. Build image: `docker build -t basic-calculator .`
2. Run container: `docker run -p 8081:8080 basic-calculator`
