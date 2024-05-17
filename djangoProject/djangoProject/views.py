from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello, world. You are at About Page")

def contact(request):
    return HttpResponse("Hello, world. You are at contact")