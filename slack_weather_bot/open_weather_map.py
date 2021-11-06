import logging
from typing import Any, Dict, Optional

import requests

LOG = logging.getLogger(__name__)


class OpenWeatherMap:
    """
    A client for the Open Weather Map API.
    """

    def __init__(self, api_key: str):
        self._api_key = api_key

    def weather_by_city_name(self, city: str) -> Optional[Dict[Any, Any]]:
        """
        Looks up the current weather for the given `city`.
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
            return response.json()
        elif response.status_code == requests.codes.NOT_FOUND:
            return None
        else:
            LOG.error("Received an unexpected response code: %d", response.status_code)
            raise Exception
