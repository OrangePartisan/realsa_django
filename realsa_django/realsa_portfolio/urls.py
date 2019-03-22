from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^index/$', views.index, name='index'),
    url(r'^realsa_blog/', views.realsa_blog, name='realsa_blog'),
    url(r'^contact/$', views.contact, name='contact'),
]