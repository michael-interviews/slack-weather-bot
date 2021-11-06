# Slack Weather Bot

## Running the bot server

Export the following environment variables:

* `SLACK_SIGNING_SECRET`
* `SLACK_BOT_TOKEN`
* `OWM_API_KEY`
* `PORT`
* `LOG_LEVEL`

Generate a Slack app manifest with:

```sh
./gen_manifest <server-url>
```

### Using [poetry](https://github.com/python-poetry/poetry)

```sh
poetry run python -m slack_weather_bot
```

### Using [docker-compose](https://docs.docker.com/compose/)

```sh
docker-compose up
```

## Formatting and linting

```sh
poetry run isort slack_weather_bot
poetry run black slack_weather_bot
poetry run pylint slack_weather_bot
poetry run mypy slack_weather_bot
```

