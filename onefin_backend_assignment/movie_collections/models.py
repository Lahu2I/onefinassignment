from django.db import models
from uuid import uuid4

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=150, null=False)
    description = models.TextField()
    genres = models.CharField(max_length=300)
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    def __str__(self):
        return self.title


class Collection(models.Model):
    title = models.CharField(max_length=150, null=False)
    description = models.TextField()
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.title