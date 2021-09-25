from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Todo

def root(request):
  all_todos_list = Todo.objects.all()
  context = {'all_todos_list': all_todos_list}
  return render(request, 'pages/root.html', context)

def detail(request, todo_id):
  todo = get_object_or_404(Todo, pk=todo_id)
  return render(request, 'pages/detail.html', {'todo': todo})

def add_todo(request):
  print(request.POST)
  desc = request.POST['todo_name']
  t = Todo(desc= desc, flag_complete=False)
  t.save()
  return redirect('root')

def edit_todo(request, todo_id):
  desc = request.POST['todo_name']
  t = Todo.objects.filter(id=todo_id)[0]
  t.desc = desc
  t.save()
  return redirect(f'/{todo_id}/')

def edit_complete(request, todo_id):
  t = Todo.objects.filter(id=todo_id)[0]
  t.flag_complete = not t.flag_complete
  t.save()
  return redirect(f'/{todo_id}/')

def delete(request, todo_id):
  t = Todo.objects.filter(id=todo_id)[0]
  t.delete()
  print('delete fxn running')
  return redirect('/')