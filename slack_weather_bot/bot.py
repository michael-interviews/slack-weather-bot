import logging

from slack_bolt import App

from slack_weather_bot.open_weather_map import OpenWeatherMap

LOG = logging.getLogger(__name__)


class WeatherBot:
    """
    Slack bot with a slash command for getting the temperature in a given city.
    """

    def __init__(self, owm_client: OpenWeatherMap):
        self._owm_client = owm_client

    def register_handlers(self, app: App):
        """
        Registers the `WeatherBot`s handlers on the given Slack `App`.
        """

        app.command("/jumo_weather")(self.get_weather)

    def get_weather(self, ack, respond, command):
        """
        Slash command handler that sends the temperature for a given city to the channel it is invoked in.
        """

        ack()
        LOG.info("Received weather slash command")
        LOG.debug("Weather slash command: %s", command)
        city = command.get("text")
        try:
            weather = self._owm_client.weather_by_city_name(city)
            LOG.debug("Weather info: %s", weather)
            if weather:
                city = weather["name"]
                country = weather["sys"]["country"]
                temp = weather["main"]["temp"]
                emoji = "🥶" if temp < 20.0 else "🌞"
                respond(
                    f"The temperature in {city} ({country}) is {temp}°C {emoji}",
                    response_type="in_channel",
                )
            else:
                respond(f"I could not find the weather in {city} 😔")
        except Exception as error:  # pylint: disable=broad-except
            LOG.error("Exception raised while looking up weather: %s", error)
            respond("Ooops, something went wrong 😵")
