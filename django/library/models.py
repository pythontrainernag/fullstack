# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from docutils.nodes import address

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    url = models.CharField(max_length=50)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    
