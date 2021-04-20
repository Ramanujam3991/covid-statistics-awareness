import uuid, base64
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline
import pymongo
import pandas as pd
import matplotlib as mpl

mpl.rcParams['font.size'] = 7.0

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png) #encodes our byte like object
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


#Covid Reports Process
def get_columns_covid2(res_by):
    if res_by == '#1':
        key = 'TotalCases'
    elif res_by == '#2':
        key = 'TotalDeaths'
    elif res_by == '#3':
        key = 'TotalRecovered'
    elif res_by == '#4':
        key = 'NewCases'
    elif res_by == '#5':
        key = 'NewDeaths'
    elif res_by == '#6':
        key = 'newRecoveredTomorrow'        
    return str(key)

def get_chart_covid2(chart_type, data, column_list,data_source, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(8,5))
    #boolVal = (column_list in ['#4', '#5', '#6'])
    key = get_columns_covid2(column_list)
    print(type(key))
    x = ['North America', 'Asia', 'South America', 'Europe', 'Africa', 'Australia/Oceania', 'nan', 'All', 'Oceania', 'World','Total:']
    data = data[~data["Country,Other"].isin(x)]
    new_data = data.nlargest(10,key)
    #print('='*50)
    #print(new_data["Country,Other"].unique())
    #print('='*50)    
    #print('#'*10,len(new_data),'#'*10)
    #print('='*50)
    #print(new_data["Country,Other"].unique())
    #print('='*50)
    y_label = "Total number of "+key
    if chart_type == '#1':
        print('bar chart')
        plt.ticklabel_format(style = 'plain')
        plt.title("Covid-19 data: Top ten 10 countries")
        #x1 = new_data['country']
        #y1 = new_data['cases']
        #plt.bar(x1,y1)
        x1 = np.array(new_data['Country,Other'])
        y1 = np.array(new_data[key])
        plt.bar(x1,y1)
        #plt.ylabel('Total no of cases')
        plt.ylabel(y_label)
        plt.xlabel('Countries')        
    elif chart_type == '#2':
        fig = plt.figure(figsize=(8,5))
        print('pie chart')
        plt.title(key)
        #plt.title("Total Covid-19 cases: Top ten 10 countries", bbox={'facecolor':'0.8', 'pad':5})        
        plt.pie(data=new_data, x=key, labels=new_data['Country,Other'].values, autopct='%.2f%%',radius=1) #,labeldistance=1.1)  | autopct='%1.0f%%'
    elif chart_type == '#3':        
        print('line chart')
        fig = plt.figure(figsize=(7,3))
        plt.title("Covid-19 data: Top ten 10 countries")
        x1 = np.array(new_data['Country,Other'])
        y1 = np.array(new_data[key])        
        plt.ticklabel_format(style = 'plain')
        plt.plot(x1,y1, color='green', marker='o', linestyle='dashed')
        plt.xlabel('Countries')  # add X-axis label
        plt.ylabel(y_label)         
    else:
        print('ups... failed to identify the chart type')
    plt.tight_layout()
    chart = get_graph()
    return chart


def read_mongodb(collection_list):
    DB_URL = "mongodb+srv://dev:dev@cluster0.73vby.mongodb.net/sampleDB?retryWrites=true&w=majority"
    DB_NAME = "sampleDB"
    databaseServer = pymongo.MongoClient(DB_URL)
    database = databaseServer[DB_NAME]
    collection = database[collection_list]
    out = list(collection.find())
    databaseServer.close()
    return out

def scipy_data(column_list):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(7,3))
    key = get_columns_covid2(column_list)    
    #DB_URL = "mongodb+srv://dev:dev@cluster0.73vby.mongodb.net/sampleDB?retryWrites=true&w=majority"
    #DB_NAME = "sampleDB"
    #databaseServer = pymongo.MongoClient(DB_URL)
    #database = databaseServer[DB_NAME]
    col_list = ['web_crawler_5th_day', 'web_crawler_4th_day', 'web_crawler_3rd_day', 'web_crawler_yesterday', 'web_crawler']
    x = ['North America', 'Asia', 'South America', 'Europe', 'Africa', 'Australia/Oceania', 'nan', 'All', 'Oceania', 'World','Total:']
    total_cases = []
    x_axis = "Country,Other"
    y_label = "Number of "+key
    for col_name in col_list:
        #collection = database[col_name]
        #out = list(collection.find())
        out = read_mongodb(col_name)
        mf =  pd.DataFrame(out)
        print('='*20,col_name,'='*20)
        mf = mf[~mf[x_axis].isin(x)]
        total_cases.append(mf[key].sum())
    #databaseServer.close()
    x = np.array([1,5,7,10,15])
    y = np.array(total_cases)    
    fun1 = interp1d(x, y,kind = 'linear')  
    fun2 = interp1d(x, y, kind = 'cubic')  
    xnew = np.linspace(1, 15,100)  
    plt.ticklabel_format(style = 'plain')
    plt.plot(x, y, 'o', xnew, fun1(xnew), '-', xnew, fun2(xnew), '--')  
    plt.legend(['data', 'linear', 'cubic','nearest'], loc = 'best')  
    plt.xlabel('Day Number')  # add X-axis label
    plt.ylabel(y_label)
    plt.tight_layout()
    chart = get_graph()
    return chart

def ml_data(column_list):
    pass