"""rakbookoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from shelf import views as shelf
from author import views as author
from book import views as book
from tags import views as tags

router = routers.DefaultRouter()
router.register(r'users', shelf.UserViewSet)
router.register(r'shelf', shelf.ShelfViewSet)
router.register(r'author', author.AuthorViewSet)
router.register(r'tags', tags.TagViewSet)
router.register(r'book', book.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
