import jwt
import logging

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework import status

from django.conf import settings

from onefin_backend_assignment.common import messages
from onefin_backend_assignment.utils import custom_exceptions as ce

from accounts.helpers.query_helpers.register_helper import get_user_object


# Get an instance of logger
logger = logging.getLogger('accounts')


class SafeJWTAuthentication(BaseAuthentication):
    '''
    first get access token and then it is decode
    after verify which user accessed log in and 
    return user object
    '''
    def authenticate(self, request):
        try:
            authorization_header = request.headers.get('Authorization')
            if authorization_header:
                access_token = authorization_header.split(' ')[1]
                payload = jwt.decode(
                    access_token, settings.SECRET_KEY, algorithms=['HS256'])
                user = get_user_object(user_id=payload.get('user_id'))

                if user:
                    return (user, None)

                raise exceptions.NotFound({
                    "success": False,
                    "status_code": status.HTTP_200_OK,
                    "message": messages.USER_NOT_FOUND,
                    "data": None})

            raise exceptions.AuthenticationFailed({
                "success": False,
                "status_code": status.HTTP_401_UNAUTHORIZED,
                "message": messages.AUTHENTICATION_INVALID,
                "data": None})

        except jwt.ExpiredSignatureError as e:
            logger.error('ACCOUNTS - AUTHENTICATION: {}'.format(e))
            raise ce.ExpiredSignatureError

        except jwt.InvalidSignatureError as e:
            logger.error('ACCOUNTS - AUTHENTICATION: {}'.format(e))
            raise ce.ExpiredSignatureError

        except jwt.DecodeError as e:
            logger.error('ACCOUNTS - AUTHENTICATION: {}'.format(e))
            raise ce.InvalidSignatureError

        except jwt.InvalidTokenError as e:
            logger.error('ACCOUNTS- AUTHENTICATION: {}'.format(e))
            raise ce.InvalidTokenError
