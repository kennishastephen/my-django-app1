
from django.shortcuts import render
from .models import Task
from datetime import date

def task_list(request):
    today = date.today()
    tasks = Task.objects.filter(created_at=today)
    total = tasks.count()
    completed = tasks.filter(completed=True).count()
    not_completed = total - completed

    return render(request, 'todo/task_list.html', {
        'tasks': tasks,
        'total': total,
        'completed': completed,
        'not_completed': not_completed
    })
