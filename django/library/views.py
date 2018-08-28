# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Author

# Create your views here.

def first(request):
    return HttpResponse("<h1>This is a first page in app</h>")

def sec(request):
    return HttpResponse("<h1>This is a sec page in app</h>")

def first_html(request):
    return render(request, 'first.html')

def sec_html(request):
    return render(request, 'second.html', {'name': "Nag"})

def log_html(request, *args, **kwargs):
    name = kwargs['name']
    return render(request, 'second.html', {'name': name})

def author_data(request):
    x = Author.objects.all()
    return render(request, 'author.html', {'objs': x})