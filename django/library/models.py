# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    url = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.first_name

class Book(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    
    def __str__(self):
        return self.name