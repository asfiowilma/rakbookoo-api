from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner}'s {self.name} tag"

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'owner']