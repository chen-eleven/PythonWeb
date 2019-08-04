from django.shortcuts import render
from django.http import JsonResponse
import datetime
from .models import CommentPlus

# Create your views here.
def get_comments(request, table_id):
    '''获取现有的评论'''
    comm_plus_li = CommentPlus.objects.get_comm_by_id(table_id)
    
    context = {
            'comm_plus_li':comm_plus_li,
            }
    return('应该是通过ajax.get方法来获取,先临时dedail')

def add_comments(request, table_id):
    context = {'table_id':table_id}
    return render(request,'home/comm.html', context)
    
def subm_comments(request,table_id):
    user = request.session['username']
    comment = request.POST.get('content')
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    table_name = 'debug'
    
    if not user :
        return JsonResponse({'errmsg':'you need to login'})
    if len(str(comment)) <= 4:
        return JsonResponse({'errmsg':'the length need to be greater than 4'})
    comm_statu = CommentPlus.objects.add_one_comm(
            table_id=table_id, table_name=table_name, 
            user=user, create_time=create_time, 
            comment=comment)
    
    return JsonResponse({'errmsg':"Comment written successfully"})