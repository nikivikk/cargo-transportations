FROM python:3.10.2-slim-buster

WORKDIR ./

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=manage.py

EXPOSE 4000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]


