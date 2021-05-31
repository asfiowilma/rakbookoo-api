from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Tag, TagSerializer

# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]