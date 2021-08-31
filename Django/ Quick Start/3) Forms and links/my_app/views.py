from django.shortcuts import render, redirect
from .models import Author, Article

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def add_blog_post(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    if request.method == 'GET':
        return render(request, 'pages/posts.html', context)
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        author = request.POST['author']
        result = Author.objects.get(id = author)
        Article.objects.create(author = result, title = title, text = text, pub_date = pub_date)
        return redirect('posts')

def register_author(request):
    if request.method == 'GET': 
        return render(request, 'pages/register.html')
    elif request.method == 'POST':
        first_name = request.POST['first_name']  
        last_name = request.POST['last_name']    
        email = request.POST['email']
        Author.objects.create(first_name = first_name, last_name = last_name, email = email)
        return redirect('posts')
