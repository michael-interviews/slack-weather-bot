import datetime
import logging
from typing import List, Optional

import requests
from pydantic import BaseModel

LOG = logging.getLogger(__name__)


# Models
# WARNING: incomplete


class Sys(BaseModel):
    """
    Internal fields.
    """

    country: str
    sunrise: datetime.datetime
    sunset: datetime.datetime


class Main(BaseModel):
    """
    Temperature, pressure and humidity information.
    """

    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int


class Weather(BaseModel):
    """
    Description of weather.
    """

    main: str
    description: str


class WeatherByCityName(BaseModel):
    """
    Response from a `OpenWeatherMap.weather_by_city_name` call.
    """

    name: str
    weather: List[Weather]
    main: Main
    sys: Sys


# Client


class OpenWeatherMap:
    """
    A client for the Open Weather Map API.
    """

    def __init__(self, api_key: str):
        self._api_key = api_key

    def weather_by_city_name(self, city: str) -> Optional[WeatherByCityName]:
        """
        Looks up the current weather for the given `city`.

        Raises:
            pydantic.ValidationError if the response fails validation.
            Exception if the response has an unexpected status code.
        """

        LOG.debug("Looking up weather for '%s'", city)
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": city,
                "units": "metric",
                "appid": self._api_key,
            },
        )
        LOG.debug("Weather response: %s", response)
        # pylint: disable=no-member
        if response.status_code == requests.codes.OK:
            return WeatherByCityName(**response.json())
        elif response.status_code == requests.codes.NOT_FOUND:
            return None
        else:
            LOG.error("Received an unexpected response code: %d", response.status_code)
            raise Exception
