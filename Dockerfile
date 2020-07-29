# Std image file --> 1.13Go
#FROM python:3.7.7 

# Alpine image (need g++ for numpy)
# FROM python:3.7.7-alpine
# RUN apk add g++ 
# NOT WORKING

# with slim buster 371 Mo :-)
FROM python:3.7-slim-buster

WORKDIR /app
# COPY SRC DEST
COPY . .
WORKDIR /app/flask_app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-c", "gunicorn.conf.py", "wsgi:server"]