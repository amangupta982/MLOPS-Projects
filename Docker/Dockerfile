FROM python:3.9-slim

# workdir
WORKDIR /app

#copy
COPY . /app

#run
RUN pip install -r requirements.txt

#port
EXPOSE 8080

# commands
CMD ["python3", "app.py"]
