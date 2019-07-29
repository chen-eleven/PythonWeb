from django.shortcuts import render


# Create your views here.
def bar(request):
    context={'a':'此处是一个测试点',
             'data18':[18203, 23489, 29034, 104970, 131744, 630230]
             }
    return render(request, 'report/echarts.html', context)
    #return render(request, 'report/test.html', context)
