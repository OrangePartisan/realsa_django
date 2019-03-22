from django.conf.urls import url, include
from . import views
#from django.views.generic import ListView, DetailView
#from realsa_blog.models import RealsaBlog

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
]