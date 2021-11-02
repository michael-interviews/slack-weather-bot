import logging
import sys

from slack_bolt import App

from slack_weather_bot.config import Config

LOG = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    logging.Formatter(fmt="{asctime} [{levelname}] {message}", style="{")
)
LOG.addHandler(handler)


def main() -> int:
    try:
        config = Config.load_from_env()
    except Exception as e:
        LOG.error(str(e))
        return 1

    LOG.setLevel(config.log_level)

    app = App(
        token=config.bot_token,
        signing_secret=config.signing_secret,
    )
    app.command("/jumo_weather")(get_weather)
    app.start(port=config.port)

    return 0


def get_weather(ack, respond, command):
    LOG.info("received weather slash command")
    LOG.debug(f"weather slash command: {command}")
    ack()
    city = command.get("text")
    respond(f"TODO: look up weather for {city}")


if __name__ == "__main__":
    sys.exit(main())
