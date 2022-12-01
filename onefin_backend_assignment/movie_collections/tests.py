import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Collection, Movie


class CollectionTest(APITestCase):

    def setUp(self):
        self.movie1 = Movie.objects.create(title='Queerama')
        self.movie2 = Movie.objects.create(title='Satana likuyushchiy')
        self.movie3 = Movie.objects.create(title='Betrayal')

    def test_can_create_collection(self):
        url = reverse('movie_collection:collection')
        data = {
            'title': 'Test Collection',
            'description': 'The body of the test Collection.',
            'movies': [{
            "title":"tuze meri kasam",
            "description": "including heroes and heroine ",
            "genres":"Romantic",
            "uuid":""
        }],
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)