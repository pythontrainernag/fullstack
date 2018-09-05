'''
Created on Aug 29, 2018

@author: nexii
'''
from django import forms
from .models import Publisher, Book

class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=50, min_length=2)
    last_name = forms.CharField(max_length=50, min_length=2)
    email = forms.EmailField()
    
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"
    
class simpleForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=50, min_length=2)
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        #fields = ['name', 'publisher']
        exclude = ['author']
    