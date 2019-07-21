from django.shortcuts import render

from .models import HotTables
# Create your views here.
def index(request):
    '''显示首页'''
    '''查询四个类型的表'''
    rn_table_hot = HotTables.objects.get_table_by('rn', 8, 'length')
    order_table_hot = HotTables.objects.get_table_by('order', 8, 'length')
    other_table_hot = HotTables.objects.get_table_by('other', 8, 'length')
    report_table_hot = HotTables.objects.get_table_by('report', 8, 'length')
    context = {
            'rn_table_hot':rn_table_hot ,
            'order_table_hot' : order_table_hot,
            'other_table_hot' : other_table_hot,
            'report_table_hot' : report_table_hot,
            }
       
    
    
    # 使用loger session
    return render(request, 'home/index.html', context)


    