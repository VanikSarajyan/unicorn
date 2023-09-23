from urllib import parse
from wsgiref.headers import Headers
from http.client import responses


class Request:
    def __init__(self, env) -> None:
        self.env = env

    @property
    def args(self) -> dict:
        return {k: v[0] for k, v in parse.parse_qs(self.env["QUERY_STRING"]).items()}


class Response:
    def __init__(
        self, response=None, status=200, charset="utf-8", content_type="text/html"
    ) -> None:
        self.response = [] if response is None else response
        self.charset = charset
        self.headers = Headers()
        self.content_type = f"{content_type}; charset={charset}"
        self.headers.add_header("content_type", self.content_type)
        self._status = status

    @property
    def status(self):
        status_string = responses.get(self._status, "UNKNOWN")
        return f"{self._status} {status_string}"

    def __iter__(self):
        for k in self.response:
            if isinstance(k, bytes):
                yield k
            else:
                yield k.encode(self.charset)


def unicorn(function):
    def application(env, start_response):
        request = Request(env)
        response = function(request)
        start_response(response.status, response.headers.items())
        return response

    return application


@unicorn
def app(request: Request) -> Response:
    name = request.args.get("name", "PyCon")
    return Response([f"<h1>Hello, {name}</h1>"])
