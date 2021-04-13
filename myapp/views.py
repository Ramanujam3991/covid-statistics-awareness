from django.shortcuts import render

# Create your views here.

from django.urls import path

from . import views
from .models import Todo


def hello(request):
    todo = Todo.objects.all()
    context = {
        'covid_data_list': todo
    }
    print('context data:::',context)
    return render(request, "hello.html",context)