from django.urls import path
from movie_collections.apiviews.collections import CollectionAPIView
from movie_collections.apiviews.movies import MoviesAPIView

urlpatterns = [
    path('collection/', CollectionAPIView.as_view(), name='collection'),
    path('collection/<uuid:uuid>', CollectionAPIView.as_view()),
    path('movies/', MoviesAPIView.as_view(), name='movie')
]
