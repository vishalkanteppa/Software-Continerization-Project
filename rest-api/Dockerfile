FROM python:slim

RUN apt-get update

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 1337

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:1337", "--log-file", "/dev/termination-log", "--access-logfile", "/dev/termination-log", "--workers", "4", "--keep-alive", "0"]