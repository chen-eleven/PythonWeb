from django.shortcuts import render, redirect
from django.urls import reverse
import re
from users.models import Passport #, Address
from django.http import HttpResponse, JsonResponse
from utils.decorators import login_required
#from order.models import OrderInfo, OrderGoods
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from users.tasks import send_active_email
from django.core.mail import send_mail
from django.conf import settings
import os
from django_redis import get_redis_connection
# from home.models import Books

# Create your views here.
def register(request):
    '''显示用户注册页面'''
    return render(request, 'users/register.html')

def register_handle(request):
    '''进行用户注册处理'''
    # 接收数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    # 进行数据校验
    if not all([username, password, email]):
        # 有数据为空
        return render(request, 'users/register.html', {'errmsg':'参数不能为空!'})

    # 判断邮箱是否合法
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        # 邮箱不合法
        return render(request, 'users/register.html', {'errmsg':'邮箱不合法!'})

    p = Passport.objects.check_passport(username=username)

    if p:
        return render(request, 'users/register.html', {'errmsg': '用户名已存在！'})

    # 进行业务处理:注册，向账户系统中添加账户
    # Passport.objects.create(username=username, password=password, email=email)
    Passport.objects.add_one_passport(username=username, password=password, email=email)

    # 生成激活的token itsdangerous
    
# =============================================================================
#     serializer = Serializer(settings.SECRET_KEY, 3600)
#     token = serializer.dumps({'confirm':passport.id}) # 返回bytes
#     token = token.decode()
# 
#     # 给用户的邮箱发激活邮件
#     # send_mail('尚硅谷书城用户激活', '', settings.EMAIL_FROM, [email], html_message='<a href="http://127.0.0.1:8000/user/active/%s/">http://127.0.0.1:8000/user/active/</a>' % token)
#     send_active_email.delay(token, username, email)
# =============================================================================

    # 注册完，还是返回注册页。
    return redirect(reverse('home:index'))

def login(request):
    '''显示登录页面'''
    username = ''
    checked = ''

    context = {
        'username': username,
        'checked': checked,
    }

    return render(request, 'users/login.html', context)

# /user/logout
def logout(request):
    '''用户退出登录'''
    # 清空用户的session信息
    request.session.flush()
    # 跳转到首页
    return redirect(reverse('home:index'))

def login_check(request):
    '''进行用户登录校验'''
    # 1.获取数据
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    verifycode = request.POST.get('verifycode')

    # 2.数据校验
    if not all([username, password, remember, verifycode]):
        # 有数据为空
        return JsonResponse({'res': 2})

    if verifycode.upper() != request.session['verifycode']:
        return JsonResponse({'res': 2})

    # 3.进行处理:根据用户名和密码查找账户信息
    passport = Passport.objects.get_one_passport(username=username, password=password)

    if passport:
        # 用户名密码正确
        # 获取session中的url_path
        # if request.session.has_key('url_path'):
        #     next_url = request.session.get('url_path')
        # else:
        #     next_url = reverse('books:index')
        if passport.is_active:
            next_url = reverse('home:index') # /user/
            jres = JsonResponse({'res': 1, 'next_url': next_url})
        
            # 判断是否需要记住用户名
            if remember == 'true':
                # 记住用户名
                jres.set_cookie('username', username, max_age=7*24*3600)
            else:
                # 不要记住用户名
                jres.delete_cookie('username')
        
            # 记住用户的登录状态
            request.session['islogin'] = True
            request.session['username'] = username
            request.session['passport_id'] = passport.id
            return jres
        else:
            return JsonResponse({'res': 3})    # 没激活
    else:
        # 用户名或密码错误
        return JsonResponse({'res': 0})



def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'Ubuntu-RI.ttf'), 15)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

def register_active(request, token):
    '''用户账户激活'''
    serializer = Serializer(settings.SECRET_KEY, 3600)
    try:
        info = serializer.loads(token)
        passport_id = info['confirm']
        # 进行用户激活
        passport = Passport.objects.get(id=passport_id)
        passport.is_active = True
        passport.save()
        # 跳转的登录页
        return redirect(reverse('user:login'))
    except SignatureExpired:
        # 链接过期
        return HttpResponse('激活链接已过期')

