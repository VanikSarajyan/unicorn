from wsgiref.headers import Headers
from http.client import responses


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
