from .forms import TaskForm
from django.shortcuts import render, redirect
from .models import Task

# from django.views.generic.list import ListView

def TaskListForm(request):
    context = {}
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('taskview')
    context['form']= form
    return render(request, "todo/todo_form.html", context)



def TaskListView(request):
    todo_views = Task.objects.all()
    context = {'todo_views':todo_views}
    return render(request, "todo/taskview.html", context)

def DetailView(request, id):
    detail = Task.objects.get(id = id)
    return render (request, 'todo/detail.html', {'todo': detail})


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