from django.shortcuts import render, redirect
from django.urls import reverse
from django_redis import get_redis_connection

from .models import HotTables
from .models import Tables,TableDetails
from django.views.decorators.cache import cache_page
from utils.decorators import login_required
import logging

logger = logging.getLogger('django.request')

# Create your views here.
@login_required
#@cache_page(60 * 15)
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
       
    # 使用loger session  这里会导致注册的时候要打印报错
# =============================================================================
# #    logger.info(request.session['username'])
# #    logger.info(request.body)
# =============================================================================

    return render(request, 'home/index.html', context)

#@login_required
def detail(request, table_id):
    '''显示表的详情页面'''
    # 获取业务表的详情信息
    clos = TableDetails.objects.get_table_by_id(table_id=table_id)
    table = Tables.objects.get_table_by_id(table_id=table_id)[0]
    
    #将颜色标签替换掉
    clos_tmp = []
    for i in clos:
        if i.level == 1:
            i.level ="yellow"
        else:
            i.level ="white"
        clos_tmp.append(i)
    


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
    context = {'clos': clos_tmp, 'table':table}

    # 使用模板
    return render(request, 'home/detail.html', context)
    

# 商品种类 页码 排序方式
# /list/(种类id)/(页码)/?sort=排序方式
from django.core.paginator import Paginator

#@login_required
def list(request, db_type, db_name, page):
    '''商品列表页面'''
    # 获取排序方式
    #sort = request.GET.get('sort', 'default')

    # 判断type_id是否合法
# =============================================================================
#     if int(type_id) not in BOOKS_TYPE.keys():
#         return redirect(reverse('books:index'))
# 
# =============================================================================
    # 根据商品种类id和排序方式查询数据
    books_li = Tables.objects.get_tables_by_type(db_type=db_type,db_name=db_name,)
    # 获取去重的所有库名，列在list页左边
    db_name_all = Tables.objects.get_db_name_all(db_type)
    # 分页
    paginator = Paginator(books_li, 100)

    # 获取分页之后的总页数
    num_pages = paginator.num_pages

    # 取第page页数据
    if page == '' or int(page) > num_pages:
        page = 1
    else:
        page = int(page)

    # 返回值是一个Page类的实例对象
    tables_li = paginator.page(page)

    # 进行页码控制
    # 1.总页数<5, 显示所有页码
    # 2.当前页是前3页，显示1-5页
    # 3.当前页是后3页，显示后5页 10 9 8 7 6
    # 4.其他情况，显示当前页前2页，后2页，当前页
    if num_pages < 5:
        pages = range(1, num_pages+1)
    elif page <= 3:
        pages = range(1, 6)
    elif num_pages - page <= 2:
        pages = range(num_pages-4, num_pages+1)
    else:
        pages = range(page-2, page+3)

    # 新品推荐
    #books_new = Books.objects.get_books_by_type(db_name=db_name, limit=2, sort='new')

    # 定义上下文
    #type_title = BOOKS_TYPE[int(type_id)]
    context = {
        'tables_li': tables_li,
        'db_name_all':db_name_all,
        #'books_new': books_new,
        'db_type': db_type,
        'db_name' : db_name,
        'sort': 'table_name',
        'type_title': 'debug',
        'pages': pages
    }

    # 使用模板
    return render(request, 'home/list.html', context)


def  more(request,code):
    code_dict = {1:'您可能没有权限用您提供的凭据核验进入。。。',
               2:'该域名可能还处于开发中。。。'}
    context =  {'msg':code_dict[int(code)]}
    return render(request, 'more/more.html',context)