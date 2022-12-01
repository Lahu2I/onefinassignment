import logging
import datetime
from passlib.hash import pbkdf2_sha256
import jwt
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from onefin_backend_assignment.common import messages
from onefin_backend_assignment.utils import custom_exceptions as ce
from accounts.helpers.query_helpers.register_helper import get_user_object
from accounts import serializers

# Get an instance of logger
logger = logging.getLogger('accounts')


def generate_access_token(user):
    '''used for generating access token'''
    access_token_payload = {
        'user_id': user.id,
        'user_password': user.password,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(
            days=0, minutes=settings.ACCESS_TOKEN_EXPIRES),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = (
        jwt.encode(access_token_payload, settings.SECRET_KEY,
        algorithm='HS256')
    )
    
    return access_token


def login_request(request):
    '''
    used for user token register
    '''
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': messages.ENTER_INVALID,
                'data': None},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = get_user_object(username=username)
        
        if not user:
            instance = user_register(request)
            user = get_user_object(username=instance.data['username'])
        
        access_token = generate_access_token(user)

        data = {
            'access_token': access_token
        }

        return Response({
            'success': True,
            'status_code': status.HTTP_201_CREATED,
            'message': messages.ACCESS_TOKEN_GENERATED,
            'data': data},
            status=status.HTTP_201_CREATED
        )

    except Exception as e:
        logger.error('LOGIN FUNCTION HELPER : LOGIN REQUEST{}'.format(e))
        raise ce.InternalServerError


def user_register(request):
    '''
    used for user register instance
    '''
    try:
        serializer = serializers.RegistrationSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()

        return serializer
            
    except Exception as e:
        logger.error('REGISTER FUNCTION HELPER : REGISTER REQUEST{}'.format(e))
        return None