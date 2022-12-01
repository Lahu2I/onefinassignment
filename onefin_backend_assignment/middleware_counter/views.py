import logging
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Get an instance of logger
logger = logging.getLogger('middleware_counter')


class CounterRequest(APIView):
    '''
    This API count the number of requests served
    by server

    method(get)
    '''
    def get(self,request):
        count = request.session.get('count')

        return Response({
            'requests': f" total number of requests \
served by this server till now is {count}"
        })


class ResetCounterRequest(APIView):

    '''
    This API reset count the number of requests served
    by server
    
    method(post)
    '''
    def post(self,request):

        del request.session['count']

        return Response({
            'message': 'request count reset successfully'
        })