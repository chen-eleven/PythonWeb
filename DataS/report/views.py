from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pandas
import datetime


# Create your views here.
def bar(request):
    sto_time = datetime.datetime.now().strftime('%Y-%m-%d')
    sta_time = (datetime.datetime.now() - datetime.timedelta(days=7)) \
        .strftime('%Y-%m-%d')
    
    data = pandas.read_excel('templates/report/data.xls')
    data['time'] = data['time'].dt.strftime('%Y%m%d')
    data =  data[(data['time']>='20190720') & (data['time']<='20190727')]
    data2 = data.to_dict(orient='records')
    
    
    context={'a':'此处是一个测试点',
             'start_time': sta_time,
             'stop_time': sto_time,
             'data18':[18203, 23489, 29034, 104970, 131744, 630230],
             'test':[{'a':1,'b':2},
                     {'a':10,'b':20},
                     ],
             'testb':{'a':{'aa':10},'b':222},
             'data2':data2,
             }
    return render(request, 'report/echarts.html', context)
    #return render(request, 'report/test.html', context)

def bar_time_filter(request):
    # 接收数据
    sta_time = request.POST.get('start_time')
    sto_time = request.POST.get('stop_time')
    print('----------------',sta_time)  
    data = pandas.read_excel('templates/report/data.xls')
    data['time'] = data['time'].dt.strftime('%Y-%m-%d')
    data =  data[(data['time']>= sta_time) & (data['time']<= sto_time)]
    data2 = data.to_dict(orient='records')
    data3 = data.to_dict(orient='list')
    
   
    context={'a':'此处是一个测试点',
             'start_time': sta_time,
             'stop_time': sto_time,
             'data18':[18203, 23489, 29034, 104970, 131744, 630230],
             'test':[{'a':1,'b':2},
                     {'a':10,'b':20},
                     ],
             'testb':{'a':{'aa':10},'b':222},
             'data2':data2,
             'data3':data3,
             'data4':[1,2,5,5],
             'data5':['蒸发量','降水量','平均温度'],
             'data7':'水量测试'
             }
    print('11111111111111111',data3['address'],type(data3['address']),context['data4'])
    return render(request, 'report/echarts.html', context)
    #return JsonResponse(context)