FROM python:3.7

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD . /app

RUN pip install git+https://github.com/resurfaceio/logger-python
RUN python manage.py db init && python manage.py db stamp head && python manage.py db migrate && python manage.py db upgrade

EXPOSE 5000