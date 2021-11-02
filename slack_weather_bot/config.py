import dataclasses
import os


@dataclasses.dataclass
class Config:
    bot_token: str
    signing_secret: str
    log_level: str
    port: int

    @staticmethod
    def load_str_from_env(name: str) -> str:
        var = os.environ.get(name)
        if not var:
            raise Exception(f"Environment variable '{name}' not set")
        return var

    @classmethod
    def load_from_env(cls) -> "Config":
        bot_token = cls.load_str_from_env("SLACK_BOT_TOKEN")
        signing_secret = cls.load_str_from_env("SLACK_SIGNING_SECRET")
        log_level = os.environ.get("LOG_LEVEL", "DEBUG")
        port_str = cls.load_str_from_env("PORT")

        try:
            port = int(port_str)
            if not (0 < port < 2 ** 16):
                raise ValueError
        except ValueError:
            raise Exception(f"'{port_str}' is not a valid port number")

        return Config(
            bot_token=bot_token,
            signing_secret=signing_secret,
            log_level=log_level,
            port=port,
        )
