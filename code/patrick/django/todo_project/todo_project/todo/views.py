from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView
# posts = [
#     {
#         'title': 'Test1',
#         'text_desc': 'the is a test',
#         'created_date': 'September 1, 2021',
#         'completed_date': 'September 2, 2021',
#         'author': 'test user'
#     },
#     {
#         'title': 'Test2',
#         'text_desc': 'the is a test',
#         'created_date': 'September 1, 2021',
#         'completed_date': 'September 2, 2021',
#         'author': 'test user'
#     }
# ]




def home(request):
    context = {
        'posts': Post.objects.all()
    
    }
    return render(request, 'todo/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'todo/home.html'
    context_object_name = 'posts'
    ordering = ['complete', 'created_date']

class PostDetailView(DetailView):
    model = Post
 


def about(request):
    return render(request, 'todo/about.html', {'title': 'About'})