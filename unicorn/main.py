from urllib import parse


def app(env, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/html; charset=utf8")]
    start_response(status, headers)

    GET = parse.parse_qs(env["QUERY_STRING"])
    name = GET.get("name", ["PyCon"])[0]

    return [f"<h1>Hello {name}!</h1>".encode("utf-8")]
