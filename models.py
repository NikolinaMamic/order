from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class FirstModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    popis = models.TextField(max_length=1000, null=True)
