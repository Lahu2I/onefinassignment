import uuid
import logging
from rest_framework.response import Response
from rest_framework import status
from onefin_backend_assignment.common import messages

from onefin_backend_assignment.utils import custom_exceptions as ce
from movie_collections.helpers.query_helpers.collections_helper import (
    create_collection_query, add_movie_collection_mapping,
    fetch_collection_query, fetch_movie_favorite_genres, 
    raw_fetch_movie_query,raw_fetch_collection_query
)

# Get an instance of logger
logger = logging.getLogger('movie_collections')


def add_collection(request):
    '''
    this is used for creating collection with movie
    request(json): get request from user
    '''

    try:
        add_collection_details = {}

        request.data['uuid'] = str(uuid.uuid4())
        add_collection_details['uuid'] = request.data['uuid']

        title = (
            request.data.get('title').strip() 
            if request.data.get('title') else None
        )
        if title:
            add_collection_details['title'] = title
        
        description = (
            request.data.get('description').strip() 
            if request.data.get('description') else None
        )
        if description:
            add_collection_details['description'] = description

        collection_details = create_collection_query(
            add_collection_details=add_collection_details
        )

        for movies_data in request.data.get('movies'):
            mapping_uuid = uuid.uuid4()
            
            add_mapping_details = {
                'title': movies_data['title'],
                'description': movies_data['description'],
                'genres': movies_data['genres'],
                'uuid': mapping_uuid
            }
            instance = add_movie_collection_mapping(add_mapping_details)
            collection_details.movies.add(instance)

        return Response({    
            'success': True,
            'collection_uuid':collection_details.uuid,
            })

    except Exception as e:
        logger.error('COLLECTION FUNCTION HELPER : ADD COLLECTION {}'.format(e))
        raise ce.InternalServerError

    
def fetch_collection(request,uuid=None):
    '''
    this is used for retriving single collection
    or all collection
    '''
    try:
        collection_data = fetch_collection_query(uuid=uuid)

        if uuid:
            return Response(collection_data)
        
        favourite_genres = fetch_movie_favorite_genres(request)
        
        return Response({    
            'is_success': True,
            'data':collection_data,
            'favourite_genres':favourite_genres
            })
            
    except Exception as e:
        logger.error('COLLECTION FUNCTION HELPER : FETCH COLLECTION {}'.format(e))
        raise ce.InternalServerError


def delete_collection(request, uuid=None):
    '''
    this is used for delete single collection
    '''
    
    try:
        collection_data = raw_fetch_collection_query(uuid=uuid)

        if not collection_data:
            return Response({
                'success': False,
                'message': messages.DATA_NOT_FOUND,
                'status_code': status.HTTP_400_BAD_REQUEST,
            })

        collection_data.delete()

        return Response({
            'success': True,
            'status_code': status.HTTP_201_CREATED,
            'message': messages.DELETE_RECORD,
        })

    except Exception as e:
        logger.error('COLLECTION FUNCTION HELPER : DELETE COLLECTION {}'.format(e))
        raise ce.InternalServerError


def update_collection(request, uuid=None):
    '''
    this is used for update single collection
    or all collection with movie
    '''
    try:
        collection_data = raw_fetch_collection_query(uuid=uuid)
        
        if not collection_data:
            return Response({
                'success': False,
                'message': messages.DATA_NOT_FOUND,
                'status_code': status.HTTP_400_BAD_REQUEST,
            })

        collection_data.title = request.data.get('title')
        collection_data.description = request.data.get('description')
        collection_data.save()

        for movies_data in request.data.get('movies'):

            movies_data = raw_fetch_movie_query(
                uuid=movies_data['uuid']
            )
            movies_data.title = movies_data['title']
            movies_data.description = movies_data['description']
            movies_data.genres = movies_data['genres']
            movies_data.save()
            collection_data.movies.set(movies_data)

        return Response({
            'success': True,
            'message': messages.UPDATE_RECORD,
        })

    except Exception as e:
        logger.error('COLLECTION FUNCTION HELPER : UPDATE COLLECTION {}'.format(e))
        raise ce.InternalServerError