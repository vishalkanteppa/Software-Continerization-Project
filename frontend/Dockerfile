FROM python:slim

RUN apt-get update

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 1337

CMD ["flask", "run"]

