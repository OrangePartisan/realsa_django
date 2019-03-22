"""realsa_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from realsa_useraccount import views as user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^realsa_portfolio/', include('realsa_portfolio.urls')),
    url(r'^\Z', include('realsa_portfolio.urls')),
    url(r'^realsa_blog/', include('realsa_blog.urls'), name='realsa_blog'),
    url(r'^realsa_useraccount/', user_views.get_name, name='get_name'),
]