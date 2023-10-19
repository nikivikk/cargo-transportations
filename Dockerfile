FROM python:3.10.2-slim-buster

WORKDIR /cargo-transportations

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=manage.py

EXPOSE 4000

CMD [ "python", "manage.py"]


