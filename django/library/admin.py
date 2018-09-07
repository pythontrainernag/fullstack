# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book,Publisher,Author
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'publisher')
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_name')
    search_fields  = ('first_name',)
    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)


