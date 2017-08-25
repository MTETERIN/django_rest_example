# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^', views.APIKEYView.as_view(), name='api_key'),
]
