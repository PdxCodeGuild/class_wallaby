from django.shortcuts import render, redirect
from .models import Author, Note
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def register_author(request):
    if request.method == 'GET':
        return render(request, 'pages/register.html')
    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Author.objects.create(first_name=first_name, last_name=last_name,)
        return redirect('add_posts')


def add_note(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    if request.method == 'GET':
        return render(request, 'pages/add_note.html', context)
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        author = request.POST['author']
        result = Author.objects.get(id=author)
        Note.objects.create(author=result, title=title,
                            text=text, pub_date=pub_date)
        return redirect('view_all')


def view_all(request):
    authors = Author.objects.all()
    return render(request, 'pages/all.html', {'authors': authors})


def post_details(request, id):
    post = Note.objects.get(id=id)
    return render(request, 'pages/post_details.html', {"post": post})


def update_post(request, id):
    if request.method == 'GET':
        return render(request, 'pages/post_details.html')
    elif request.method == 'POST':
        post = Note.objects.get(id=id)
        post.text = request.POST['edit_description']
        post.save()
        return redirect('view_all')


def delete_post(request, id):
    post = Note.objects.get(id=id)
    post.delete()
    return redirect('view_all')
