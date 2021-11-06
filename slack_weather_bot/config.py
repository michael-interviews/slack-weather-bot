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

        return Config(
            bot_token=_get_env_or_raise("SLACK_BOT_TOKEN"),
            signing_secret=_get_env_or_raise("SLACK_SIGNING_SECRET"),
            open_weather_map_api_key=_get_env_or_raise("OWM_API_KEY"),
            log_level=os.environ.get("LOG_LEVEL", "INFO"),
            port=_parse_port(os.environ.get("PORT", "8080")),
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


def _parse_port(port_str: str) -> int:
    """
    Parses and validates the given `port_str` and returns the port as an `int`.

    Examples:
        >>> _parse_port("1")
        1
        >>> _parse_port("65535")
        65535
        >>> _parse_port("not a port")
        Traceback (most recent call last):
            ...
        config.InvalidPortNumberError: 'not a port' is not a valid port number
        >>> _parse_port("0")
        Traceback (most recent call last):
            ...
        config.InvalidPortNumberError: '0' is not a valid port number
        >>> _parse_port("65536")
        Traceback (most recent call last):
            ...
        config.InvalidPortNumberError: '65536' is not a valid port number

    Raises:
        InvalidPortNumberError if `port_str` is not a valid port number.
    """

    try:
        port = int(port_str)
        if not 0 < port < 2 ** 16:
            raise ValueError
        return port
    except ValueError as error:
        raise InvalidPortNumberError(port_str) from error
