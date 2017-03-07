from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(r'Rango says hey there partner!<br><a href="about">About</a>')

def about(request):
    return HttpResponse(r'Rango says here is the about page.<br><a href="/rango/">Home</a>')