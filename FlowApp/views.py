from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.
def home(request):
    tasks = Todo.objects.all()
    ordering = ['-id']
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks':tasks, 'form':form}


    return render(request, 'FlowApp/home.html', context)

def updateTask(request, pk):
    task = Todo.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}

    return render(request, 'FlowApp/Update.html', context)

def deleteTask(request, pk):
    todo_task = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo_task.delete()
        return redirect('/')

    context = {'todo_task':todo_task}

    return render(request, 'FlowApp/Affirm.html', context)
