from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.

from django.urls import path

from . import views
from .models import Todo
from .forms import TodoForm

"""
def hello(request):
    todo = Todo.objects.all()
    context = {
        'covid_data_list': todo
    }
    print('context data:::',context)
    return render(request, "hello.html",context)
"""
def addnew(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                pass
    else:
        form = TodoForm()

    return render(request,'index.html',{'form':form})
def index(request):
    report = Todo.objects.all()
    return render(request,'show.html',{'report':report})
def edit(request, id):
    report = Todo.objects.get(id=id)
    return render(request,'edit.html', {'report':report})
def update(request, id):
    report = Todo.objects.get(id=id)
    form = TodoForm(request.POST, instance = report)
    if form.is_valid():
        form.save()
        return redirect("/")
    print(form.errors.as_data())
    return render(request, 'edit.html', {'report': report})
def destroy(request, id):
    report = Todo.objects.get(id=id)
    report.delete()
    return redirect("/")