from django.shortcuts import render, redirect
from .models import Author, Book

def home(request):
    return render(request, 'pages/index.html')

def check_out_in(request):
    books = Book.objects.all()
    context = {'books': books}
    if request.method == 'GET':
        return render(request, 'pages/check_out_in.html', context)
    elif request.method == 'POST':
        ...

def view_all(request):
    books = Book.objects.all()
    return render(request, 'pages/all_books.html', {'books': books})

def details(request, id):
    ...