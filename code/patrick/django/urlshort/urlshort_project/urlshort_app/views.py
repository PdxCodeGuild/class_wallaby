from django.shortcuts import render, redirect 
from .models import Short


def home(request):
    return render (request, 'urlshort_app/index.html') 