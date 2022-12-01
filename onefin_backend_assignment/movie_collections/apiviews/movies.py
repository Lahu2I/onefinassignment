import logging
from rest_framework.views import APIView

from onefin_backend_assignment.utils import custom_exceptions as ce
from movie_collections.helpers.function_helpers.movies_helper import (
    fetch_movies_data_third_api
)

# Get an instance of logger
logger = logging.getLogger('movie_collections')


class MoviesAPIView(APIView):
    '''
    Methods
    -------
    get:
    Return a list of all the existing movie
    from third party API
    '''
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        '''
        request(post):
        Create a new collection and movie instance
        '''
        try:
            response = fetch_movies_data_third_api(request)
            
            return response

        except Exception as e:
            logger.error('MOVIES API VIEW : GET {}'.format(e))
            raise ce.InternalServerError