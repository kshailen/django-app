from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def all_sectors(request):
    return render(request, 'greno/all_greno.html')

