from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Shelf

class ShelfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shelf
        fields = ['name', 'owner']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']