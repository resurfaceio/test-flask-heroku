FROM resurfaceio/python:2.3.0

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD . /app

RUN pip install git+https://github.com/resurfaceio/logger-python@master#egg=usagelogger
RUN python manage.py db init && python manage.py db stamp head && python manage.py db migrate && python manage.py db upgrade

EXPOSE 5000
CMD gunicorn --bind :5000 wsgi:application
