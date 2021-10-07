from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all() # Todo.objects.order_by('-date_entered', '-date_completed')
    context = {'todos': todos}
    return render(request, 'todos/todo.html', context)

def add_todo(request):
    if request.method == "GET":
        return render(request, 'todos/add.html')
    elif request.method == "POST":
        text = request.POST['text']
        if (request.POST['status'] == 'False'):
            status = False
        else:
            status = True
        Todo.objects.create(text = text, status = status)
        return redirect('list')

def details(request, id):
    todo = Todo.objects.get(id = id)
    context = {'todo': todo}
    return render(request, 'todos/detail.html', context)

def update(request, id):
    todo = Todo.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'todos/update.html', {'todo': todo})
    elif request.method == 'POST':
        todo.text = request.POST['text']
        if (request.POST['status'] == 'False'):
            todo.status = False
        else:
            todo.status = True
        todo.save()
        return redirect('details', todo.id)

def remove_todo(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect('list')