from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Author, AuthorSerializer

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]