
class CounterMiddleware(object):
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.count = 0
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        self.count += 1
        request.session['count'] = self.count
        response = self.get_response(request)

        return response