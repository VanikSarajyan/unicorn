from unicorn import unicorn, Request, Response


@unicorn
def app(request: Request) -> Response:
    name = request.args.get("name", "PyCon")
    return Response([f"<h1>Hello, {name}</h1>"])
