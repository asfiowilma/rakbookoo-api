from django.contrib.auth.models import User, Group
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


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']