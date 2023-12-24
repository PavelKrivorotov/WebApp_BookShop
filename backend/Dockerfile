# syntax=docker/dockerfile:1

FROM python:3.10-alpine3.15
WORKDIR /app/

# Add and install requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Add .env variables
COPY ./.docker.env /app/.env

# Add source files
COPY ./main/author /app/main/author
COPY ./main/book /app/main/book
COPY ./main/category /app/main/category
COPY ./main/main /app/main/main
COPY ./main/manage.py /app/main/manage.py

# Create storage directory for images 
RUN mkdir /app/main/images

ENTRYPOINT ["python3", "main/manage.py", "runserver", "0.0.0.0:8000"]
