from django.shortcuts import render, redirect

# Create your views here.

from django.urls import path

from . import views
from .forms import TodoForm
from .models import Todo, Covid


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

    return render(request,'index2.html',{'form':form})
def index(request):
    report = Todo.objects.all()
    return render(request,'show.html',{'report':report})
def edit(request,Country):
    report = Todo.objects.get(Country=Country)
    return render(request,'edit.html', {'report':report})
def update(request, Country):
    report = Todo.objects.get(Country=Country)
    form = TodoForm(request.POST, instance = report)
    if form.is_valid():
        form.save()
        return redirect("/")
    print(form.errors.as_data())
    return render(request, 'edit.html', {'report': report})
def destroy(request, Country):
    report = Todo.objects.get(Country=Country)
    report.delete()
    return redirect("/")

def api(request):
    report= Covid.objects.all()
    return render(request, 'api.html', {'report': report})
