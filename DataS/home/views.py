from django.shortcuts import render, redirect
from django.urls import reverse
from django_redis import get_redis_connection

from .models import HotTables
from .models import Tables,TableDetails
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

def detail(request, table_id):
    '''显示表的详情页面'''
    # 获取业务表的详情信息
    clos = TableDetails.objects.get_table_by_id(table_id=table_id)
    table = Tables.objects.get_table_by_id(table_id=table_id)


    if clos is None or table is None:
        # 商品不存在，跳转到首页
        return redirect(reverse('home:index'))

    # 新品推荐 可以根据表的业务类型推荐相关的表

    # 用户登录之后，才记录浏览记录
    # 每个用户浏览记录对应redis中的一条信息 格式:'history_用户id':[10,9,2,3,4]
    # [9, 10, 2, 3, 4]
    if request.session.has_key('islogin'):
        # 用户已登录，记录浏览记录
        con = get_redis_connection('default')
        key = 'history_%d' % request.session.get('passport_id')
        # 先从redis列表中移除books.id
        con.lrem(key, 0, table.table_id)
        con.lpush(key, table.table_id)
        # 保存用户最近浏览的5个商品
        con.ltrim(key, 0, 4)
        
    

    # 定义上下文
    context = {'clos': clos, 'table_li':table}

    # 使用模板
    return render(request, 'home/cp.html', context)
    