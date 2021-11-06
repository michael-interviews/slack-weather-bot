import dataclasses
import os
import typing


class EnvironmentVariableNotFoundError(Exception):
    """
    An environment varibale is unset or empty.
    """

    def __init__(self, name: str):
        super().__init__(f"Environment variable '{name}' not set")


class InvalidPortNumberError(Exception):
    """
    A number is not a valid port number.
    """

    def __init__(self, port: typing.Union[str, int]):
        super().__init__(f"'{port}' is not a valid port number")


@dataclasses.dataclass
class Config:
    """
    Environment configuration for the application.
    """

    bot_token: str
    signing_secret: str
    open_weather_map_api_key: str
    log_level: str
    port: int

    @staticmethod
    def load_from_env() -> "Config":
        """
        Returns:
            A `Config` with values read from the environment.

        Raises:
            `EnvironmentVariableNotFoundError` if a required config varible is not set or is empty.
            `InvalidPortNumberError` if the configured port number is not valid.
        """

        bot_token = _get_env_or_raise("SLACK_BOT_TOKEN")
        signing_secret = _get_env_or_raise("SLACK_SIGNING_SECRET")
        open_weather_map_api_key = _get_env_or_raise("OWM_API_KEY")
        log_level = os.environ.get("LOG_LEVEL", "INFO")
        port_str = os.environ.get("PORT", "8080")

        try:
            port = int(port_str)
            if not 0 < port < 2 ** 16:
                raise ValueError
        except ValueError as error:
            raise InvalidPortNumberError(port_str) from error

        return Config(
            bot_token=bot_token,
            signing_secret=signing_secret,
            open_weather_map_api_key=open_weather_map_api_key,
            log_level=log_level,
            port=port,
        )


def _get_env_or_raise(name: str) -> str:
    """
    Returns:
        The environment variable called `name`.

    Raises:
        `EnvironmentVariableNotFoundError` if the variable is undefined or empty.
    """
    var = os.environ.get(name)
    if not var:
        raise EnvironmentVariableNotFoundError(name)
    return var
