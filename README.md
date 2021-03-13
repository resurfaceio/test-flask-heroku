# test-flask
Test GraphQL API built with Flask

## Configure Environment

Install your Resurface database: https://resurface.io/pilot-edition

```
# configure to point to your Resurface database host
export USAGE_LOGGERS_URL=http://<resurface-host>:4001/message
```

## Deploy Locally

```
make start     # rebuild and start containers
make ping      # make simple ping request
make bash      # open shell session
make logs      # follow container logs
make stop      # halt and remove containers
```

## Deploy to Heroku

1. Create Heroku app

```
heroku create flask-resurface
```

3. Push to Heroku

```
heroku container:login
heroku stack:set container -a flask-resurface
heroku config:set USAGE_LOGGERS_URL="http://marina:4001/message"
git push heroku master
```

4. Make ping request

```
curl "http://flask-resurface.herokuapp.com/ping"
```

5. Delete Heroku app

```
heroku apps:destroy flask-resurface
```
