import logging

from movie_collections.models import Collection, Movie

# Get an instance of logger
logger = logging.getLogger('movie_collections')


def create_collection_query(
    add_collection_details=None
):
    '''
    function is used for add new collection 
    and save in database

    parameter:
    add_collection_details(dict): all collection attribute

    return:
    add new collection with specified attribute data
    '''

    try:
        data = Collection.objects.create(
            title=add_collection_details.get('title'),
            description=add_collection_details.get('description'),
            uuid=add_collection_details.get('uuid')
        )
        
    except Exception as e:
        logger.error(
            'COLLECTION QUERY HELPER : COLLECTION CREATE {}'.format(e)
        )
        data = None
    
    return data


def add_movie_collection_mapping(mapping_data=None):
    '''
    function is used, for store collection mapping data
    '''
    try:
        add_data = Movie.objects.create(**mapping_data)
        
    except Exception as e:
        logger.error(
            'COLLECTION QUERY HELPER : ADD MOVIE COLLECTION {}'.format(e)
        )
        add_data = None
        
    return add_data


def fetch_collection_query(uuid=None):
    '''
    function is used, for fetch records of collection data
    '''
    try:
        if uuid:
            fetch_data = Collection.objects.get(uuid=uuid)
            movies_data = list(fetch_data.movies.values(
                'title','description','genres','uuid')
            )

            fetch_data = {
                'title': fetch_data.title,
                'description': fetch_data.description,
                'movies': movies_data
            }
        else:
            fetch_data = Collection.objects.values('title','uuid','description')
            if fetch_data:
                fetch_data = list(fetch_data)

    except Exception as e:
        logger.error(
            'COLLECTION QUERY HELPER : FETCH MOVIE COLLECTION {}'.format(e)
        )
        fetch_data= None
        
    return fetch_data


def fetch_movie_favorite_genres(request):
    '''
    function is used for fetch movie favorite genres
    '''
    try:
        favorite_genres_data = []
        fetch_data = Movie.objects.order_by('collection__movies')
        fetch_data = fetch_data.values('genres')[0:3]
        if fetch_data:
            fetch_data = list(fetch_data)
            for data in fetch_data:
                favorite_genres_data.append(data['genres'])

    except Exception as e:
        logger.error(
            'COLLECTION QUERY HELPER : FETCH MOVIE COLLECTION {}'.format(e)
        )
        favorite_genres_data= None
        
    return favorite_genres_data


def raw_fetch_collection_query(uuid=None):
    '''
    function is used for raw fetch collection query
    '''
    try:
        fetch_data = Collection.objects.get(uuid=uuid)

    except Exception as e:
        logger.error(
            'COLLECTION QUERY HELPER : RAW FETCH COLLECTION {}'.format(e)
        )
        fetch_data= None
        
    return fetch_data


def raw_fetch_movie_query(uuid=None):
    '''
    function is used for fetch movie query
    '''
    try:
        fetch_data = Movie.objects.get(uuid=uuid)

    except Exception as e:
        logger.error(
            'COLLECTION QUERY HELPER : FETCH MOVIE COLLECTION {}'.format(e)
        )
        fetch_data= None
        
    return fetch_data

