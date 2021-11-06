# Slack Weather Bot

## Running the bot server

Export the following environment variables:

* `SLACK_SIGNING_SECRET` - Slack app signing secret.
* `SLACK_BOT_TOKEN` - Slack bot user OAuth token.
* `OWM_API_KEY` - Open Weather Map API key.
* `PORT` - Port that the bot server runs on. Default `8080`.
* `LOG_LEVEL` - Logging level. Default `INFO`.

### Using [poetry](https://github.com/python-poetry/poetry)

```sh
poetry run python -m slack_weather_bot
```

### Using [docker-compose](https://docs.docker.com/compose/)

```sh
docker-compose up
```

## Installing the app in a Slack workspace

1. Browse to <https://api.slack.com/apps>.
1. Click `Create an App`.
1. Click `From an app manifest`.
1. Select the workspace to install the app to and click `Next`.
1. Generate a Slack app manifest with:

    ```sh
    ./gen_manifest <server-url>
    ```

1. Copy and paste the manifest into the window and click `Next` and then `Create`.
1. Go to `Distribution -> Install App` and click `Install to Workspace` and then `Allow`.
1. Go to `Distribution -> Install App` and copy and save the `Bot User OAuth Token`.
1. Go to `General -> Basic Information -> App Credentials` and copy and save the `Signing Secret`.

## Formatting and linting

```sh
poetry run isort slack_weather_bot
poetry run black slack_weather_bot
poetry run pylint slack_weather_bot
poetry run mypy slack_weather_bot
```

