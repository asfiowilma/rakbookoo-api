from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shelf(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{owner}'s {name} shelf"

    class Meta:
        verbose_name_plural = "shelves"