from django.shortcuts import render
import pandas
import datetime


# Create your views here.
def bar(request):
    sta_time = datetime.datetime.now().strftime('%Y-%m-%d')
    sto_time = (datetime.datetime.now() - datetime.timedelta(days=7)) \
        .strftime('%Y-%m-%d')
    
    data = pandas.read_excel('templates/report/data.xls')
    
    
    context={'a':'此处是一个测试点',
             'start_time': sta_time,
             'stop_time': sto_time,
             'data18':[18203, 23489, 29034, 104970, 131744, 630230]
             }
    return render(request, 'report/echarts.html', context)
    #return render(request, 'report/test.html', context)
