from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def state(request):
    return HttpResponse('<h1 style="background-color:red; color:yellow"><marquee>Odisha is my state</marquee></h1>')