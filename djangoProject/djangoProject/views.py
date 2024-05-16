from django.http import HttpRequest
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You are at Home")

def about(request):
    return HttpResponse("Hello, world. You are at About Page")

def contact(request):
    return HttpResponse("Hello, world. You are at contact")