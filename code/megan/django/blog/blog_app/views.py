from django.shortcuts import render, redirect
from . models import Blog
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def add_post(request):
    if request.method == "GET":
        return render(request, 'pages/add.html')
    elif request.method == "POST":
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        Blog.objects.create(title = title, text = text, pub_date = pub_date)
        return redirect('posts')

def blog_posts(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'pages/posts.html', context)

def see_details(request, id):
    post = Blog.objects.get(id = id)
    return render(request, 'pages/details.html', {"post": post})   