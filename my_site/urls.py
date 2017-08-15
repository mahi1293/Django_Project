from django.conf.urls import url
from . import views
# from jsonrpc.backend.django import api

urlpatterns = [
    url(r'^$', views.home, name='home'),
    
]
