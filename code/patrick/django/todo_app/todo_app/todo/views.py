from .forms import TaskForm, UpdateForm
from django.shortcuts import render, redirect
from .models import Task
# from django.http import HttpResponse 

# from django.views.generic.list import ListView

def TaskListForm(request):
    context = {}
    form = TaskForm(request.POST or None)
    print('test')
    if form.is_valid():
        form.save()
        return redirect('taskview')
    context['form']= form
    return render(request, "todo/todo_form.html", context)



def TaskListView(request):
    todo_views = Task.objects.all()
    context = {'todo_views':todo_views}
    return render(request, "todo/taskview.html", context)


    
def Update(request, id):
    todo = Task.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'todo/update.html', {'todo': todo})
    elif request.method == 'POST':
        
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        print(todo.description)
        if (request.POST['complete'] == 'False'):
            todo.complete = False
        else:
            todo.complete = True
        todo.save()
        return redirect('taskview')
        
def Remove(request, id):
    todo = Task.objects.get(id = id)
    todo.delete()
    return redirect('taskview')


# def Add_list(request):
#     if request.method =='Get':
#         return render (request, 'todo_forms.py')

# def TaskViews(request):
#     if request.method =='POST':
#         user = request.POST['user']
#         title = request.POST['title']
#         description = request.POST['description']
#         complete = request.POST['complete']
#         create = request.POST['create']
#     return print(user=user, title=title, description=description, complete=complete, create=create)

# def TaskViews(request):
#     print(request.GET)
#     return render(request, "todo_view.html")