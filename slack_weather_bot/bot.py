import logging

from slack_bolt import App

from slack_weather_bot.open_weather_map import OpenWeatherMap

LOG = logging.getLogger(__name__)


class WeatherBot:
    def __init__(self, app: App, owm_client: OpenWeatherMap):
        self._owm_client = owm_client
        app.command("/jumo_weather")(self.get_weather)

    def get_weather(self, ack, respond, command):
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
        except Exception as e:
            LOG.error("Exception raised while looking up weather: %s", e)
            respond("Ooops, something went wrong 😵")
