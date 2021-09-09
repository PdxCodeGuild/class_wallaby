from django.shortcuts import render, redirect
from .models import Author, Article
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'pages/home.html')

@login_required
def about(request):
    return render(request, 'pages/about.html')

@login_required
def add_blog_post(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    if request.method == 'GET':
        return render(request, 'pages/add_blog_post.html', context)
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        author = request.POST['author']
        result = Author.objects.get(id = author)
        Article.objects.create(author = result, title = title, text = text, pub_date = pub_date)
        return redirect('view_all')

@login_required
def register_author(request):
    if request.method == 'GET': 
        return render(request, 'pages/register.html')
    elif request.method == 'POST':
        first_name = request.POST['first_name']  
        last_name = request.POST['last_name']    
        email = request.POST['email']
        Author.objects.create(first_name = first_name, last_name = last_name, email = email)
        return redirect('add_posts')

@login_required
def view_all(request):
    authors = Author.objects.all()
    return render(request, 'pages/all.html', {"authors": authors})

@login_required
def post_details(request, id): ##we get the id of the element. Remember, all elements are created with an ID in the database.
    post = Article.objects.get(id = id) ## we are assigning the item to a variable
    return render(request, 'pages/post_details.html', {"post": post}) ## we are passing the variable to the page