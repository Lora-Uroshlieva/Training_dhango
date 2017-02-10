from ln.models import Session


class Auth(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            user_session = request.COOKIES['user-session']
            session = Session.objects.filter(token=user_session).last()
            print(session.user.login)
        except KeyError:
            pass

        print (request.COOKIES['user-session'])
        user_session = request.COOKIES
        response = self.get_response(request)

        return response


# class Auth(object):
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.
#
#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#
#         response = self.get_response(request)
#
#         # Code to be executed for each request/response after
#         # the view is called.
#
#         return response