from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.


def index(request):
    tasks_data=tasks.objects.all()
    task_data_count=len(tasks_data)
    print(task_data_count)
    context={
        'tasks_data':tasks_data,
        'task_data_count':task_data_count,
    }
    return render(request,'app/index.html',context)


def adddata(request):
    if request.method == 'POST':
        text=request.POST.get('text_data')
        if text != '':
            tasks.objects.create(text=text)
            tasks_data=list(tasks.objects.values())
            return JsonResponse({'status': 'success','tasks_data':tasks_data})
        else:
            return JsonResponse({'status': 'empty_feald'})
    else:
        return JsonResponse({'status': 'failed'})

def datadelete(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        print(id)
        data=tasks.objects.get(pk=id)
        data.delete()
        tasks_data=list(tasks.objects.values())
        return JsonResponse({'status': 'deleted','tasks_data':tasks_data})
    else:
        return JsonResponse({'status': 'delete_failed'})