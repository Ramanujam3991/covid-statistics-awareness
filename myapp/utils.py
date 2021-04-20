import uuid, base64
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np

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
def get_columns_covid(res_by):
    if res_by == '#1':
        key = 'cases'
    elif res_by == '#2':
        key = 'deaths'
    elif res_by == '#3':
        key = 'recovered'
    return str(key)

def get_chart_covid(chart_type, data, column_list,data_source, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(8,5))
    key = get_columns_covid(column_list)
    print(type(key))
    new_data = data.nlargest(10,key)
    y_label = "Total number of "+key
    #key = 'cases'
    #new_data = data
    #data['Total'] = data.groupby('country')[key].transform('sum')
    #new_data = data.drop_duplicates(subset=['country','Total'])
    if chart_type == '#1':
        print('bar chart')
        plt.ticklabel_format(style = 'plain')
        plt.title("Covid-19 data: Top ten 10 countries")
        #x1 = new_data['country']
        #y1 = new_data['cases']
        #plt.bar(x1,y1)
        x1 = np.array(new_data['country'])
        y1 = np.array(new_data[key])
        plt.bar(x1,y1)
        #plt.ylabel('Total no of cases')
        plt.ylabel(y_label)
        plt.xlabel('Countries')        
    elif chart_type == '#2':
        fig = plt.figure(figsize=(8,5))
        print('pie chart')
        plt.title(key.upper())
        #plt.title("Total Covid-19 cases: Top ten 10 countries", bbox={'facecolor':'0.8', 'pad':5})
        #fig = plt.figure(figsize=(7,4))
        plt.pie(data=new_data, x=key, labels=new_data['country'].values, autopct='%1.0f%%') #,labeldistance=1.1)
    elif chart_type == '#3':        
        print('line chart')
        x1 = np.array(new_data['country'])
        y1 = np.array(new_data[key])
        fig = plt.figure(figsize=(7,3))
        plt.ticklabel_format(style = 'plain')
        plt.plot(x1,y1, color='green', marker='o', linestyle='dashed')
        plt.xlabel('Countries')  # add X-axis label
        plt.ylabel(y_label)         
    else:
        print('ups... failed to identify the chart type')
    plt.tight_layout()
    chart = get_graph()
    return chart