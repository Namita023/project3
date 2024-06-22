from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def country(request):
    return HttpResponse('<h1 style="background-color:red; color:yellow"><marquee>India is my country</marquee></h1>')