from django.http import HttpResponse
from django.shortcuts import render

# Create your views here testing edit

def home(request):
    return HttpResponse("Hello faizan")
