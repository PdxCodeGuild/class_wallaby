from django.shortcuts import render, redirect
from . models import Author, Article

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def register_author(request):
    if request.method == 'GET':
        return render(request, 'pages/register.html')
    elif request.method == 'POST':
        first_name = request.POST['first_name']