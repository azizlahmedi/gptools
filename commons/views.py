# -*- coding: utf-8 -*-
from django.shortcuts import render


def homee(request):
    return render(request, 'commons/home.html')
