import logging
from rest_framework.views import APIView

from onefin_backend_assignment.utils import custom_exceptions as ce
from movie_collections.helpers.function_helpers.collections_helper import (
    add_collection, fetch_collection, delete_collection, update_collection
)

# Get an instance of logger
logger = logging.getLogger('movie_collections')


class CollectionAPIView(APIView):
    '''
    This is a class for handling CRUD operations on collection movie data.

    Methods
    -------
    post:
    Create a new collection and movie instance.

    get:
    Return a list of all the existing collection and movie.

    get(lead_uuid):
    returns a single collection object.

    put(lead_uuid):
    updates the existing collection and movie object

    delete(lead_uuid):
    deletes the existing collection object.

    '''

    def post(self, request):
        '''
        request(post):
        Create a new collection and movie instance
        '''
        try:
            
            response = add_collection(request)
            
            return response

        except Exception as e:
            logger.error('COLLECTION API VIEW : POST {}'.format(e))
            raise ce.InternalServerError

    def get(self, request, uuid=None):
        '''
        request(get):
        Return a single colection or all the existing collection and movie.
        '''
        try:
            response = fetch_collection(request, uuid)
            
            return response

        except Exception as e:
            logger.error('COLLECTION API VIEW : GET {}'.format(e))
            raise ce.InternalServerError


    def put(self, request, uuid=None):
        '''
        put(lead_uuid):
        updates the existing collection and movie object
        '''
        try:
            response = update_collection(request, uuid)
            
            return response

        except Exception as e:
            logger.error('COLLECTION API VIEW : PUT {}'.format(e))
            raise ce.InternalServerError


    def delete(self, request, uuid=None):
        '''
        delete(lead_uuid):
        deletes the existing collection object
        '''
        try:
            response = delete_collection(request, uuid)
            
            return response

        except Exception as e:
            logger.error('COLLECTION API VIEW : DELETE {}'.format(e))
            raise ce.InternalServerError
