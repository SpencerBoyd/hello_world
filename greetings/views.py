from django.shortcuts import render

# Create your views here.
# greetings/views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")
