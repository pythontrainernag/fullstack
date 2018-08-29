'''
Created on Aug 29, 2018

@author: nexii
'''
from django import forms

class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=50, min_length=2)
    last_name = forms.CharField(max_length=50, min_length=2)
    email = forms.EmailField()
    address = forms.CharField()
    tem_address = forms.CharField(widget = forms.Textarea)
    