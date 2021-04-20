from django.shortcuts import render,redirect
from .models import Todo
from .models import Covid
# Create your views here.

from django.urls import path

from . import views
from .models import Todo
from .forms import TodoForm
from .forms import CovidForm
from .covid_forms import CovidSearchForm
import pandas as pd
from .utils import get_chart_covid
from .utils2 import get_chart_covid2,scipy_data, ml_data
import json
import pymongo
import requests
from django.shortcuts import reverse

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

def new_api(request):
    if request.method == "POST":
        form = CovidForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/api")
            except:
                pass
    else:
        form = CovidForm()

    return render(request,"new_api.html",{'form':form})


def api_edit(request,country):
    report = Covid.objects.get(country=country)
    return render(request,'api_edit.html', {'report':report})

def api_update(request,country):
    report = Covid.objects.get(country=country)
    form = CovidForm(request.POST, instance = report)
    if form.is_valid():
        form.save()
        return redirect('/api')
    print(form.errors.as_data())
    return render(request, 'api_edit.html', {'report': report})
def api_destroy(request, country):
    report = Covid.objects.get(country=country)
    report.delete()
    return redirect('/api')



def get_absolute_url():
    return reverse('covid')

def mongo_op(data_source,operation_type=""):
    out = None
    DB_URL = "mongodb+srv://dev:dev@cluster0.73vby.mongodb.net/sampleDB?retryWrites=true&w=majority"
    DB_NAME = "sampleDB"
    databaseServer = pymongo.MongoClient(DB_URL)
    database = databaseServer[DB_NAME]
    collection = database['api_covid_data']
    if(operation_type == "delete"):
        collection.drop()
    if(operation_type == "create"):
        data = requests.get('https://corona.lmao.ninja/v2/countries').text
        covid_data = json.loads(data)
        collection.insert_many(covid_data)
        out = list(collection.find())
    databaseServer.close()
    return out

def mongo_op2(col_name):
    out = None
    DB_URL = "mongodb+srv://dev:dev@cluster0.73vby.mongodb.net/sampleDB?retryWrites=true&w=majority"
    DB_NAME = "sampleDB"
    databaseServer = pymongo.MongoClient(DB_URL)
    database = databaseServer[DB_NAME]
    collection = database[col_name]
    out = list(collection.find())
    databaseServer.close()
    return out

def mongodb_view(request):
    chart_type = None
    chart = None
    mf = None
    form = CovidSearchForm(request.POST or None,initial={'column_list': 'Select'})
    if request.method == 'POST':
        column_list = request.POST.get('column_list')
        chart_type = request.POST.get('chart_type')
        data_source = request.POST.get('data_source')
        data = mongo_op(data_source,"delete")
        boolValue = data_source == "#1"
        boolValue2 = data_source == "#2"
        boolValue3 = data_source == "#3"
        boolValue4 = data_source == "#4"
        data = mongo_op(data_source,"create") if boolValue else data
        data = mongo_op2('web_crawler') if boolValue2 else data
        data = mongo_op2('web_crawler_future') if boolValue4 else data
        mf =  pd.DataFrame(data)
        chart = get_chart_covid(chart_type, mf,column_list, data_source) if boolValue else chart
        chart = get_chart_covid2(chart_type, mf,column_list, data_source) if boolValue2 or boolValue4 else chart
        print('#'*10,data_source,'#'*10)
        chart = scipy_data(column_list) if boolValue3 else chart
        #chart = ml_data(column_list) if boolValue4 else chart
    context = {
        'form':form,
        'chart':chart,
    }
    return render(request,'covid_report.html',context)