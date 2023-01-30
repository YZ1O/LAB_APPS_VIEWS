from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def hello_world(request : HttpRequest):
    result = 'Hello World, This is my new HOME !'
    return HttpResponse(result)

def about(request : HttpRequest):
    result = 'A simple paragraph about the website.'
    return HttpResponse(result)