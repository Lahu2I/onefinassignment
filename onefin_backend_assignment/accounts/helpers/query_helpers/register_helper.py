import logging

from django.conf import settings
from django.contrib.auth.models import User


# Get an instance of logger
logger = logging.getLogger('accounts')


def get_user_object(user_id=None, username=None):
    """get user instance details."""

    try:
        if user_id:
            user = User.objects.get(id=user_id) 
            return user

        if username:
            user = User.objects.get(username=username)
            return user

    except Exception as e:
        logger.error(
            'REGISTER QUERY HELPER : REGISTER LOGIN REQUEST{}'.format(e)
        )
        return None


def create_user_object(username=None,password=None):
    '''create user object using username and password'''

    try:
        User.objects.create(username=username, password=password)
        
        return {
            'username':username,
            'password':password
        }

    except Exception as e:
        logger.error(
            'REGISTER QUERY HELPER : REGISTER REQUEST{}'.format(e)
        )
        
        return None

        