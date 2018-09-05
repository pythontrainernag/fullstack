"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from .views import first, sec, first_html, sec_html, log_html, author_data, add_author, addpub, addbook, success


urlpatterns = [
    url(r'^$', first),
    url(r'^sec/$', sec),
    url(r'^fhtml/$', first_html),
    url(r'^shtml/$', sec_html),
    url(r'^n(?P<name>[A-z1-9]+)/$', log_html),
    url(r'^authors/$', author_data),
    url(r'^addauthor/$', add_author),
    url(r'^addpub/$', addpub),
    url(r'^addbook/$', addbook),
    url(r'^success/$', success),
]
