
from django.shortcuts import redirect, render
from .models import ToDoItem

# Create your views here.
def home(request):
    return render(request,'todo/home.html')

def todoView(request):
    all_todo_items = ToDoItem.objects.all()
    print(all_todo_items)
    context = {'all_items': all_todo_items}
    return render(request,'todo.html', context)

def addTodo(request):
    if request.method == 'POST':
        task = request.POST['content']
        print(task)
        ToDoItem.objects.create(content = task)
        return redirect("main-view")

def detail_todo(request, id):
    tododetails = ToDoItem.objects.get(id=id)
    print(id,tododetails,'print')
    # tododetails = {"tododetails": tododetails}
    return render(request,'details.html',{'tododetails': tododetails})
    

    

   
    