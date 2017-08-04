# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
# creation de l'url

urlpatterns = [

    url(r'^$', views.post_list, name='post_list'),
]