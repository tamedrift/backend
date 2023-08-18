FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE 0

RUN pip install poetry==1.2.2

WORKDIR /app

COPY . /app/

RUN poetry install --without dev,scripts

RUN python manage.py collectstatic --noinput

EXPOSE 8000
