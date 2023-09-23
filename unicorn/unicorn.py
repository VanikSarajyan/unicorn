from unicorn.myrequest import Request


def unicorn(function):
    def application(env, start_response):
        request = Request(env)
        response = function(request)
        start_response(response.status, response.headers.items())
        return response

    return application
