from django.db import models
from rest_framework import serializers
from author.models import Author
from tags.models import Tag 
from shelf.models import Shelf

class Book(models.Model):
    title = models.CharField(max_length=255)
    cover = models.URLField(blank=True)
    blurb = models.TextField(blank=True)
    rating = models.IntegerField(default=0, blank=True)
    author = models.ManyToManyField(Author, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{title} - {author}"

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'cover', 'blurb', 'rating', 'author', 'tags', 'shelf']