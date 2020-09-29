FROM python:3.7-slim-buster

WORKDIR /usr/app

COPY requirements.txt .
COPY setup.py .
COPY src/. src/

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .

ENV LOG_LEVEL INFO

CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:8000", "src.main:myapi"]

EXPOSE 8000