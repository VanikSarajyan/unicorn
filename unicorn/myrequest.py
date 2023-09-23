from urllib import parse


class Request:
    def __init__(self, env) -> None:
        self.env = env

    @property
    def args(self) -> dict:
        return {k: v[0] for k, v in parse.parse_qs(self.env["QUERY_STRING"]).items()}
