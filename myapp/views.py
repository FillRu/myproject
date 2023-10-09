from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Task
from .forms import TaskForm

def task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, "tasks.html", {'tasks': tasks, 'form': form})

