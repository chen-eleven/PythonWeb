from django.shortcuts import render

# Create your views here.
def index(request):
    '''显示首页'''
    cloud = ('table1', 'table2')
    context = {
            'cloud':cloud}
    
    # 使用loger session
    return render(request, 'home/index.html', context)