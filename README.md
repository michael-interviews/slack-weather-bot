# Slack Weather Bot

## Running the bot server

This project uses [poetry](https://github.com/python-poetry/poetry) to manage its dependencies.

Export the following environment variables:

* `SLACK_SIGNING_SECRET`
* `SLACK_BOT_TOKEN`
* `PORT`

Run the slack bot server with:

```sh
poetry run python -m slack_weather_bot
```

