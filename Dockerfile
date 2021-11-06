FROM python:3.8

RUN pip install poetry

WORKDIR /src
COPY pyproject.toml poetry.lock /src/
COPY slack_weather_bot/ /src/slack_weather_bot
RUN poetry install

CMD poetry run python -m slack_weather_bot

