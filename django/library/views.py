# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def first(request):
    return HttpResponse("<h1>This is a first page in app</h>")

def sec(request):
    return HttpResponse("<h1>This is a sec page in app</h>")
