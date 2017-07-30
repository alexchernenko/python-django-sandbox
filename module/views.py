# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.

def hello(request):
    return HttpResponse("Pizda")