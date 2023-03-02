# -*- coding: utf-8 -*-
from django.urls import path

from commons import views

urlpatterns = [
path('', views.homee, name='commons-home'),
]
