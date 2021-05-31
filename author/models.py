from django.db import models
from rest_framework import serializers

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{first_name} {middle_name} {last_name}"

    @property
    def cited_name(self):
        "Returns the person's name in citation format."
        return f"{last_name}, {first_name} {middle_name}"

    def __str__(self):
        return f"{self.full_name()}"

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'middle_name', 'last_name']