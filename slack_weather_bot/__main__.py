import logging
import sys

from slack_bolt import App

from slack_weather_bot.bot import WeatherBot
from slack_weather_bot.config import (
    Config,
    EnvironmentVariableNotFoundError,
    InvalidPortNumberError,
)
from slack_weather_bot.open_weather_map import OpenWeatherMap

LOG = logging.getLogger(__name__)


def main() -> int:
    """
    Runs the Slack App server.
    """

    try:
        config = Config.load_from_env()
    except (EnvironmentVariableNotFoundError, InvalidPortNumberError) as error:
        LOG.error(str(error))
        return 1

    logging.basicConfig(
        format="{asctime} [{levelname:7}] [{name}] {message}",
        style="{",
        stream=sys.stdout,
        level=config.log_level,
    )

    client = OpenWeatherMap(config.open_weather_map_api_key)
    app = App(
        token=config.bot_token,
        signing_secret=config.signing_secret,
    )

    bot = WeatherBot(client)
    bot.register_handlers(app)

    app.start(port=config.port)

    return 0


if __name__ == "__main__":
    sys.exit(main())
