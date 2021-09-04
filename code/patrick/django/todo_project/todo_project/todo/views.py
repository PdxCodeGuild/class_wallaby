from django.shortcuts import render, redirect, reverse 

from .models import Todo






def home(request):
    context = {
        'posts': Todo.objects.all()
    
    }
    return render(request, 'todo/home.html', context)



def about(request):
    return render(request, 'todo/about.html', {'title': 'About'})


def todo_list(request):
    if request.method == 'POST':
        # title =request.POST.get('title')
        # author =request.POST.get('author'),
        description = request.POST.get('description'),
        # created = request.Post.get('created'),
        # complete = request.Post.get('complete')
        if description:
            Todo.objects.created(description=description)
            return redirect('about')
    object_list = Todo.object.filters(complete=False)


    return render(request, 'todo/view.html', {'object_list': object_list})