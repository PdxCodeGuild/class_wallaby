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
        title = request.POST['title']
        text = request.POST['text']
        if (request.POST['status'] == 'False'):
            status = False
        else:
            status = True
        Todo.objects.create(title = title, text = text, status = status)
        return redirect('list')

def details(request, id):
    todo = Todo.objects.get(id = id)
    return render(request, 'todos/detail.html', {'todo': todo})

# function that grabs id of element and updates it
def update(request, id):
    todo = Todo.objects.get(id = id)
    # grab input from form
    if request.method == 'GET':
        return render(request, 'todos/update.html', {'todo': todo})
    elif request.method == 'POST':
        todo.title = request.POST['title']
        todo.text = request.POST['text']
        if (request.POST['status'] == 'False'):
            todo.status = False
        else:
            todo.status = True
        # update todo with .save()
        todo.save()
        return redirect('details', todo.id)

# function that grabs id of element and deletes it
def remove_todo(request, id):
    # target item with id
    todo = Todo.objects.get(id = id)
    #delete file with .delete()
    todo.delete()
    return redirect('list')


# # function that grabs id of element and updates it
# def update(request, id):
#     # grab input from form
#     todo_items = TodoItem.objects.all()
#     item_id = 5
#     item = TodoItem.objects.get(pk=item_id)
#     # update todo with .save()
#     todo_item.save()

# # function that grabs id of element and deletes it
# def delete(request, id):
#     # target item with id
#     # delete file with .delete()