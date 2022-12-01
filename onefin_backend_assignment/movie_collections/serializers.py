from rest_framework import serializers
from movie_collections.models import Movie, Collection


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "title",
            "description",
            "genres",
            "uuid",
        ]


class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = [
            "uuid",
            "title",
            "description",
            "movies",
        ]
    
    
    
    