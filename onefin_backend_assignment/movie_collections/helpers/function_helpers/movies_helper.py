from dotenv import load_dotenv
import os
import requests
from rest_framework.response import Response
from requests.auth import HTTPBasicAuth

load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


def fetch_movies_data_third_api(request):
    '''
    this function is used for fetching movies data 
    from third party api
    '''
   
    #response = requests.get('https://demo.credy.in/api/v1/maya/movies/',
    #    auth=HTTPBasicAuth(os.getenv('USERNAME'), os.getenv('PASSWORD'))
    #)
    
    url = 'https://demo.credy.in/api/v1/maya/movies/'
    response = requests.get(url)
    data = response.json()

    return Response(data)