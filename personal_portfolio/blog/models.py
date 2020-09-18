"""Modelos 
de Blog
"""
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()