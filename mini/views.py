from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def puji(request):
    return HttpResponse('<h1>Puji is a good girl<h1>')