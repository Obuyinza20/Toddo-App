from .models import Task
from .forms import TaskForm
from django.http  import HttpResponse
from django.shortcuts import redirect, render



def F_updateTask(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method=='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context ={'form':form}
    return render(request, 'first_app/task_form.html', context)


def signUp(request):
    
    form = TaskForm()
    if request.method == 'POST':
        form= TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    
    context= {'form':form}
    return render(request, 'first_app/signup.html', context)


