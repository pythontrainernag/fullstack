# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Author
from .forms import AuthorForm, PublisherForm, BookForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView

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

def add_author(request):
    form = AuthorForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        db_obj = Author(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])
        db_obj.save()
        return HttpResponse("Data has been successfully inserted")
    return render(request, 'addauthor.html', {'form': AuthorForm()})

def success(request):
    return render(request, 'success.html')

def addpub(request):
    form = PublisherForm(request.GET)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/lib/success/")
    return render(request, 'addpub.html', {'form': PublisherForm()})

@login_required
def addbook(request):
    form = BookForm(request.GET)
    if form.is_valid():
        form.save()
        return HttpResponse("<h1>book successfully added</h1>")
    return render(request, 'addbook.html', {'form': BookForm()})


class AuthorList(ListView):
    model = Author
    template_name = 'va.html'
    context_object_name = 'book_list'