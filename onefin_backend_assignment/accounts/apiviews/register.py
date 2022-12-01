import logging
import jwt
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from onefin_backend_assignment.utils import custom_exceptions as ce
from accounts.helpers.function_helpers.register_helper import (
    login_request
)

# Get an instance of logger
logger = logging.getLogger('accounts')


class RegisterUserAPIView(APIView):
    '''
    This class create jwt token authentication of user
    just use username and password with database.
    '''
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        '''
        Method : POST
        register user login api by using username and password and generate 
        jwt token authentication for user
        Returns: user details including access token
        '''
        try:

            response = login_request(request)
            return response

        except jwt.ExpiredSignatureError as e:
            logger.error('REGISTER USER API VIEW : POST {}'.format(e))
            raise ce.ExpiredSignatureError

        except jwt.InvalidSignatureError as e:
            logger.error('REGISTER USER API VIEW : POST {}'.format(e))
            raise ce.ExpiredSignatureError

        except jwt.InvalidTokenError as e:
            logger.error('REGISTER USER API VIEW : POST {}'.format(e))
            raise ce.InvalidTokenError
