FROM python:3.9-slim

RUN apt-get update

WORKDIR /api

COPY requirements.txt /api/requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 1337

CMD ["gunicorn", "api:api", "-b", "0.0.0.0:1337", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]