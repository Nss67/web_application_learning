FROM python:latest

WORKDIR /app

COPY ./requirements.txt /app

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install -r requirements.txt

COPY . /app

WORKDIR /app/django_tutorial

ARG DEFAULT_PORT=80

ENV PORT=${DEFAULT_PORT}

EXPOSE ${PORT}

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]