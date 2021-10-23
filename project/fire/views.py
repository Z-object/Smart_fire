from turtle import pd

import self as self
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict, HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from pip._vendor.progress.counter import Pie

from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from .models import *  # 当前目录下导入models所有类
from fire.models import *
from . import forms
from . import models
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar
from pyecharts.charts import Page, Grid

ENGINE = create_engine('mysql+pymysql://root:root@localhost:3306/blog?charset=utf8')  # 连接数据库

'''************************登录注册视图函数************************'''


# 普通用户登录函数

def index(request):
    username = request.session.get('name')
    temp1 = Firesi.objects.all()
    return render(request, 'fire/index.html', {'temp': temp1, 'username': username})


# 用户注册界面

def register1(request):
    return render(request, 'fire/register.html')


# 用户注册函数

def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    age = request.POST.get('age')
    sex = request.POST.get('sex')
    phone = request.POST.get('phone')
    u1 = Person()
    '''上传图片处理'''
    # 1.获取上传文件处理对象
    pic = request.FILES['pic']
    # 2.创建文件
    save_path = '%s/fire/%s' % (settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        # 3.获取上传文件的内容并写到创建的文件中
        for content in pic.chunks():
            f.write(content)
    # 4.保存记录
    u1.goods_pic = 'fire/%s'%pic.name
    if username:
        pass
    else:
        error1 = "请输入用户名!"
        return render(request, 'fire/register.html', {'error1': error1})
    if password:
        if len(password) < 6:
            error2 = "密码长度需大于六位!"
            content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error2': error2}
            return render(request, 'fire/register.html', content)
        else:
            pass
    else:
        error2 = "请输入用户密码!"
        content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error2': error2}
        return render(request, 'fire/register.html', content)
    if age:
        pass
    else:
        error3 = "请输入年龄!"
        content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error3': error3}
        return render(request, 'fire/register.html', content)
    if phone:
        if len(phone) != 11:
            error4 = "请输入11位电话号码!"
            content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error4': error4}
            return render(request, 'fire/register.html', content)
        else:
            pass
    else:
        error4 = "请输入电话号码!"
        content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error4': error4}
        return render(request, 'fire/register.html', content)
    if Person.objects.filter(username=username):
        error = "用户名重复!"
        content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error': error}
        return render(request, 'fire/register.html', {'error': error})
    else:
        u1.username = username
        u1.password = password
        u1.age = age
        u1.sex = sex
        u1.phonenumber = phone
        u1.save()
        return render(request, 'fire/login.html')


# 用户登录界面

def login(request):
    return render(request, 'fire/login.html')


# 用户登录函数

def login1(request):
    username = request.POST.get('username')  # 将表单处理成字典的形式，通过字典key值获取value
    password = request.POST.get('password')
    if username:
        pass
    else:
        error1 = "请输入用户名"
        return render(request, 'fire/datemanage/../templates/fire/login.html', {'error1': error1})
    if password:
        pass
    else:
        error2 = "请输入密码"
        return render(request, 'fire/datemanage/../templates/fire/login.html', {'error2': error2, 'username': username})
    user = Person.objects.filter(username=username, password=password)  # 用来筛选是否存在这样的用户
    request.session['name'] = username
    if user:  # 登录成功
        return HttpResponseRedirect("/fire/firesi")
    else:  # 登录失败
        error3 = "用户名或密码错误!"
        return render(request, 'fire/datemanage/../templates/fire/login.html', {'error3': error3})





'''************************用户个人中心**************************'''


# 个人中心函数

def personcenter(request):
    name = request.session.get('name')
    user = Person.objects.filter(username=name)
    return render(request, 'fire/datemanage/percenter.html', {'user': user})


# 用户修改密码界面函数

def alterpsdhtml(request):
    name = request.session.get('name')
    return render(request, 'fire/comuser/../templates/fire/alterpsd.html', {"username": name})


# 用户修改个人信息函数

def alterpsm(request):
    name = request.session.get('name')
    p = Person.objects.get(username=name)
    p.age = request.POST.get('age')
    p.sex = request.POST.get('sex')
    p.phonenumber = request.POST.get('number')
    p.save()
    return HttpResponseRedirect('/fire/personcenter')


# 用户修改密码函数

def alterpsd(request):
    name = request.session.get('name')
    psd1 = request.POST.get('pasd1', None)
    psd2 = request.POST.get('pasd2', None)
    if psd1 != psd2:
        error_msg = '两次输入的密码不一样'
        return render(request, 'fire/datemanage/personcenter.html', {'error': error_msg})
    else:
        Person.objects.filter(username=name).update(password=psd1)
        return render(request, 'fire/datemanage/../templates/fire/login.html')


'''************************管理员用户管理以及密码修改************************'''


def test(request):
    return render(request, 'fire/test.html')

# 登录转到管理员登录

def adindex(request):
    return render(request, 'fire/adminfile/adindex.html')


# 管理员登录
def adlogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = Ad_Per.objects.filter(username=username, password=password)  # 用来筛选是否存在这样的用户
    request.session['name'] = username
    if user:  # 登录成功
        return HttpResponseRedirect("/fire/index2")
    else:
        error = "账号或密码错误!"
        return render(request, 'fire/adminfile/adindex.html', {'error': error})

# 管理员用户管理函数
def users(request,pindex):
    username = request.session.get('name')
    user = Person.objects.all()
    p1 = Person.objects.all()
    f = p1.values_list()
    paginator = Paginator(f, 5)
    if pindex == '':
        pindex = 1
    else:
        pindex = int(pindex)
    num = paginator.num_pages
    page = paginator.page(pindex)
    return render(request, 'fire/adminfile/users.html', {'page': page, 'num': num, 'user': user, 'username': username})


# 跳转到增加用户界面
def user_save(request):
    return render(request, 'fire/adminfile/newuser.html')


# 增加用户函数
def save_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    age = request.POST.get('age')
    sex = request.POST.get('sex')
    phone = request.POST.get('phone')
    u1 = Person()
    '''上传图片处理'''
    # 1.获取上传文件处理对象
    pic = request.FILES['pic']
    # 2.创建文件
    save_path = '%s/fire/%s' % (settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        # 3.获取上传文件的内容并写到创建的文件中
        for content in pic.chunks():
            f.write(content)
    # 4.保存记录
    u1.goods_pic = 'fire/%s' % pic.name
    if username:
        pass
    else:
        error1 = "请输入用户名!"
        return render(request, 'fire/register.html', {'error1': error1})
    if password:
        if len(password) < 6:
            error2 = "密码长度需大于六位!"
            content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error2': error2}
            return render(request, 'fire/register.html', content)
        else:
            pass
    else:
        error2 = "请输入用户密码!"
        content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error2': error2}
        return render(request, 'fire/register.html', content)
    if age:
        pass
    else:
        error3 = "请输入年龄!"
        content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error3': error3}
        return render(request, 'fire/register.html', content)
    if phone:
        if len(phone) != 11:
            error4 = "请输入11位电话号码!"
            content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error4': error4}
            return render(request, 'fire/register.html', content)
        else:
            pass
    else:
        error4 = "请输入电话号码!"
        content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error4': error4}
        return render(request, 'fire/register.html', content)
    if Person.objects.filter(username=username):
        error = "用户名重复!"
        content = {'username': username, 'password': password, 'age': age, 'phone': phone, 'error': error}
        return render(request, 'fire/register.html', {'error': error})
    else:
        u1.username = username
        u1.password = password
        u1.age = age
        u1.sex = sex
        u1.phonenumber = phone
        u1.save()
        return HttpResponseRedirect('/fire/users')


# 管理员删除用户函数
def delete(request):
    id1 = request.GET.get('id')
    obj = Person.objects.get(id=id1)
    obj.delete()
    return HttpResponseRedirect("/fire/users")


# 管理员修改密码界面
def adminpsd(request):
    return render(request, 'fire/adminfile/adminalterpsd.html')


# 管理员修改密码
def adminaltpsd(request):
    name = request.session.get('name')
    psd1 = request.POST.get('pasd1')
    psd2 = request.POST.get('pasd2')
    if psd1 != psd2:
        error = "两次输入密码不一致，请重新输入!"
        return render(request, 'fire/adminfile/adminalterpsd.html', {'error': error})
    else:
        a = Ad_Per.objects.filter(username=name).update(password=psd1)
        return render(request, 'fire/adminfile/adindex.html')


'''************************用户案例查询************************'''


# 火灾基本情况
def firesi(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    f1 = Firesi.objects.all()
    range1 = None
    range2 = None
    range3 = None
    ifEllipsis = 0
    f = f1.values_list()
    # 一页八条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis1 = 0
    return render(request, 'fire/datemanage/firesi.html', locals())


# 火灾基本情况详细情况
def firesidetail1(request):
    id = request.GET.get('id')
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    f = Firesi.objects.filter(id=id)
    e = Firesi.objects.get(id=id).build_char_set.all()
    return render(request, 'fire/datemanage/firesidetail1.html', {'f1': f, 'e1': e, 'user': user, 'username': username})


# 火灾基本情况搜索函数
def search(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    if request.method == 'POST':
        title = request.POST.get('title')
        if type == '':
            return HttpResponseRedirect('/fire/firesi')
    else:
        title = request.GET.get('title')
        if type == '':
            return HttpResponseRedirect('/fire/firesi')
    f1 = Firesi.objects.filter(title__icontains=title)
    f = f1.values_list()
    range1 = None
    range2 = None
    range3 = None
    lastButOne = 0
    # 一页八条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/datemanage/search.html', locals())


# 作战指挥情况
def fight(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    fc = Fight_com.objects.all()
    f = fc.values_list()
    # 一页十条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/datemanage/fight.html', locals())


# 作战指挥情况详情:
def fightdetail1(request):
    id = request.GET.get('id')
    username = request.session.get('name')
    f = Fight_com.objects.filter(id=id)
    fs = Fight_com.objects.get(id=id).fire_save_set.all()
    sq = Fight_com.objects.get(id=id).save_eq_set.all()
    pq = Fight_com.objects.get(id=id).person_eq_set.all()
    return render(request, 'fire/datemanage/fightdetail1.html', {'f1': f, 'fs1': fs, 'sq1': sq, 'pq1': pq, 'username': username})


# 作战指挥情况搜索函数
def fightsearch(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    if request.method == 'POST':
        area = request.POST.get('area')
        if area == '':
            return HttpResponseRedirect('/fire/fight')
    else:
        area = request.GET.get('area')
        if area == '':
            return HttpResponseRedirect('/fire/fight')
    f1 = Fight_com.objects.filter(area__icontains=area)
    f = f1.values_list()
    range1 = None
    range2 = None
    range3 = None
    lastButOne = 0
    # 一页八条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/datemanage/fightsearch.html', locals())


# 火灾经验总结
def exper(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    e1 = Experience.objects.all()
    f = e1.values_list()
    range1 = None
    range2 = None
    range3 = None
    lastButOne = 0
    # 一页十条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/datemanage/exper.html', locals())


# 经验总结情况详情
def experdetail1(request):
    id = request.GET.get('id')
    username = request.session.get('name')
    e = Experience.objects.filter(id=id)
    return render(request, 'fire/datemanage/experdetail1.html', {'e1': e, 'username': username})


# 经验总结情况搜索函数
def exper_search(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title == '':
            return HttpResponseRedirect('/fire/exper')
    else:
        title = request.GET.get('title')
        if title == '':
            return HttpResponseRedirect('/fire/exper')
    f1 = Experience.objects.filter(title__icontains=title)
    f = f1.values_list()
    range1 = None
    range2 = None
    range3 = None
    lastButOne = 0
    # 一页十条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/datemanage/exper_search.html', {'Page': Page, 'ifEllipsis': ifEllipsis, 'range1': range1, 'range2': range2,
                                               'range3': range3,
                                               'lastButOne': lastButOne,
                                               'title': title,
                                               'user': user})


'''************************管理员管理火灾基本情况函数************************'''


# 管理员登录函数
def index2(request):
    range1 = None
    range2 = None
    range3 = None
    ifEllipsis = 0
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    e1 = Firesi.objects.all()
    f = e1.values_list()
    # 一页十条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis1 = 0
    return render(request, 'fire/adminfile/index2.html', {'Page': Page,
                                              'ifEllipsis': ifEllipsis,
                                              'range1': range1,
                                              'range2': range2,
                                              'range3': range3,
                                              'lastButOne': lastButOne,
                                              'user': user})


# 跳转到管理员更新火灾基本情况界面
def updateFiresi(request):
    username = request.session.get('name')
    id = request.GET.get('id')
    f = Firesi.objects.filter(id=id)
    b = Firesi.objects.get(id=id).build_char_set.all()
    return render(request, 'fire/adminfile/updateFiresi.html', {'f1': f, 'b1': b, 'username': username})


# 管理员更新火灾基本情况
def updatefire(request):
    id = request.GET.get('id')
    f = Firesi.objects.get(id=id)
    f.title = request.POST.get('title')
    f.place = request.POST.get('place')
    f.detal_place = request.POST.get('detal_place')
    f.date = request.POST.get('date')
    f.time = request.POST.get('time')
    f.fire_type = request.POST.get('fire_type')
    f.fire_level = request.POST.get('fire_level')
    f.last_time = request.POST.get('last_time')
    f.major_th = request.POST.get('major_th')
    f.fire_build = request.POST.get('fire_equip')
    f.water = request.POST.get('water')
    f.save()
    f.air.wind = request.POST.get('wind')
    f.air.wind_dir = request.POST.get('wind_dir')
    f.air.weather_con = request.POST.get('weather_con')
    f.air.temper = request.POST.get('temper')
    f.air.hum = request.POST.get('hum')
    f.air.save()
    b1 = Firesi.objects.get(id=id).build_char_set.all()
    for b2 in b1:
        id2 = b2.id
    b = Build_char.objects.get(id=id2)
    b.com_bulid = request.POST.get('combuild')
    b.old_build = request.POST.get('oldbuild')
    b.wuzi_ck = request.POST.get('wzck')
    b.product_cq = request.POST.get('scck')
    b.chugq = request.POST.get('cgq')
    b.hall_build = request.POST.get('highbuild')
    b.save()
    return HttpResponseRedirect('/fire/index2')


# 管理员增加火灾基本情况界面
def alterfiresi1(request):
    return render(request, 'fire/adminfile/alterfiresi.html')


# 管理员增加火灾基本情况
def alterfiresi(request):
    a = Air()
    a.hum = request.POST.get('hum')
    a.wind = request.POST.get('wind')
    a.temper = request.POST.get('temper')
    a.wind_dir = request.POST.get('wind_dir')
    a.weather_con = request.POST.get('weather_con')
    a.save()
    f = Firesi()
    f.title = request.POST.get('title')
    f.place = request.POST.get('place')
    f.detal_place = request.POST.get('detal_place')
    f.date = request.POST.get('date')
    f.time = request.POST.get('time')
    f.fire_type = request.POST.get('fire_type')
    f.fire_level = request.POST.get('fire_level')
    f.last_time = request.POST.get('last_time')
    f.major_th = request.POST.get('major_th')
    f.fire_build = request.POST.get('fire_equip')
    f.water = request.POST.get('water')
    f.air = a
    f.save()
    b = Build_char()
    b.com_bulid = request.POST.get('combuild')
    b.old_build = request.POST.get('oldbuild')
    b.wuzi_ck = request.POST.get('wzck')
    b.product_cq = request.POST.get('scck')
    b.chugq = request.POST.get('cgq')
    b.hall_build = request.POST.get('highbuild')
    b.bfire = f
    b.save()
    return HttpResponseRedirect('/fire/index2')


# 管理员删除火灾基本情况案例
def deletefiresi(request):
    id = request.GET.get('id')
    Firesi.objects.get(id=id).delete()
    return HttpResponseRedirect('/fire/index2')

# 火灾基本情况详细情况
def firesidetail(request):
    id = request.GET.get('id')
    username = request.session.get('name')
    f = Firesi.objects.filter(id=id)
    e = Firesi.objects.get(id=id).build_char_set.all()
    return render(request, 'fire/adminfile/firesidetail.html', {'f1': f, 'e1': e, 'username': username})

# 火灾基本情况搜索函数
def adfisearch(request):
    range1 = None
    range2 = None
    range3 = None
    lastButOne = 0
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    if request.method == 'POST':
        title = request.POST.get('title')
        if type == '':
            return HttpResponseRedirect('/fire/firesi')
    else:
        title = request.GET.get('title')
        if type == '':
            return HttpResponseRedirect('/fire/firesi')
    f1 = Firesi.objects.filter(title__icontains=title)
    f = f1.values_list()
    # 一页十条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/adminfile/adfisearch.html', {'Page': Page,
                                                          'ifEllipsis': ifEllipsis,
                                                          'range1': range1,
                                                          'range2': range2,
                                                          'range3': range3,
                                                          'lastButOne': lastButOne,
                                                          'user': user,
                                                          'title': title})

'''************************管理员管理作战指挥情况函数************************'''


# 管理员跳转到作战指挥函数
def adminfight(request):
    range1 = None
    range2 = None
    range3 = None
    lastButOne = 0
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    e1 = Fight_com.objects.all()
    f = e1.values_list()
    # 一页十条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/adminfile/adminfight.html', {'Page': Page,
                                              'ifEllipsis': ifEllipsis,
                                              'range1': range1,
                                              'range2': range2,
                                              'range3': range3,
                                              'lastButOne': lastButOne,
                                              'user': user})


# 管理员更新作战指挥情况界面
def updatef(request):
    username = request.session.get('name')
    id = request.GET.get('id')
    f = Fight_com.objects.filter(id=id)
    fs = Fight_com.objects.get(id=id).fire_save_set.all()
    sq = Fight_com.objects.get(id=id).save_eq_set.all()
    pq = Fight_com.objects.get(id=id).person_eq_set.all()
    return render(request, 'fire/adminfile/updatefight.html',
                  {'f1': f, 'fs1': fs, 'sq1': sq, 'pq1': pq, 'username': username})


# 管理员修改作战指挥案例
def updatefight(request):
    id = request.GET.get('id')
    f = Fight_com.objects.get(id=id)
    f.time = request.POST.get('time')
    f.person = request.POST.get('person')
    f.see_com = request.POST.get('see_com')
    f.area = request.POST.get('area')
    f.fire_zs = request.POST.get('fire_zs')
    f.fire_change = request.POST.get('fire_change')
    f.team.area = request.POST.get('area')
    f.team.develop = request.POST.get('develop')
    f.team.person = request.POST.get('person')
    f.team.fire_recon = request.POST.get('fire_recon')
    f.team.danger = request.POST.get('danger')
    f.team.fight_task = request.POST.get('fight_task')
    f.team.build_map = request.POST.get('build_map')
    f.save()
    fs1 = f.fire_save_set.all()
    sq1 = f.save_eq_set.all()
    pq1 = f.person_eq_set.all()
    for fs2 in fs1:
        id2 = fs2.id
    fs = Fire_save.objects.get(id=id2)
    fs.消防人员 = request.POST.get('消防人员')
    fs.专家 = request.POST.get('专家')
    fs.交警 = request.POST.get('交警')
    fs.公安 = request.POST.get('公安')
    fs.医疗 = request.POST.get('医疗')
    fs.安监 = request.POST.get('安监')
    fs.政府 = request.POST.get('政府')
    fs.群众 = request.POST.get('群众')
    fs.部队 = request.POST.get('部队')
    fs.save()
    for sq2 in sq1:
        id3 = sq2.id
    sq = Save_eq.objects.get(id=id3)
    sq.水罐车 = request.POST.get('水罐车')
    sq.二氧化碳消防车 = request.POST.get('二氧化碳消防车')
    sq.云梯消防车 = request.POST.get('云梯消防车')
    sq.干粉消防车 = request.POST.get('干粉消防车')
    sq.泡沫干粉联用消防车 = request.POST.get('泡沫干粉联用消防车')
    sq.泡沫水罐车 = request.POST.get('泡沫水罐车')
    sq.登高平台消防车 = request.POST.get('登高平台消防车')
    sq.通讯消防车 = request.POST.get('通讯消防车')
    sq.高倍水罐车 = request.POST.get('高倍水罐车')
    sq.save()
    for pq2 in pq1:
        id4 = pq2.id
    pq = Person_eq.objects.get(id=id4)
    pq.呼吸器 = request.POST.get('呼吸器')
    pq.头盔 = request.POST.get('头盔')
    pq.手防护 = request.POST.get('手防护')
    pq.足防护 = request.POST.get('足防护')
    pq.防护服 = request.POST.get('防护服')
    pq.save()
    return HttpResponseRedirect('/fire/adminfight')


# 管理员增加作战指挥案例界面
def alterfight1(request):
    return render(request, 'fire/adminfile/alterfight.html')


# 管理员增加作战指挥案例
def alterfight(request):
    t = First_team()
    t.area = request.POST.get('area')
    t.develop = request.POST.get('develop')
    t.person = request.POST.get('person')
    t.fire_recon = request.POST.get('fire_recon')
    t.danger = request.POST.get('danger')
    t.fight_task = request.POST.get('fight_task')
    t.build_map = request.POST.get('build_map')
    t.save()
    f = Fight_com()
    f.time = request.POST.get('time')
    f.person = request.POST.get('person')
    f.see_com = request.POST.get('see_com')
    f.area = request.POST.get('area')
    f.fire_zs = request.POST.get('fire_zs')
    f.fire_change = request.POST.get('fire_change')
    f.team = t
    fs = Fire_save()
    fs.消防人员 = request.POST.get('消防人员')
    fs.群众 = request.POST.get('群众')
    fs.部队 = request.POST.get('部队')
    fs.专家 = request.POST.get('专家')
    fs.政府 = request.POST.get('政府')
    fs.交警 = request.POST.get('交警')
    fs.公安 = request.POST.get('公安')
    fs.医疗 = request.POST.get('医疗')
    fs.安监 = request.POST.get('安监')
    fs.save_team = f
    f.save()
    sq = Save_eq()
    sq.水罐车 = request.POST.get('水罐车')
    sq.高倍水罐车 = request.POST.get('高倍水罐车')
    sq.通讯消防车 = request.POST.get('通讯消防车')
    sq.登高平台消防车 = request.POST.get('登高平台消防车')
    sq.泡沫水罐车 = request.POST.get('泡沫水罐车')
    sq.泡沫干粉联用消防车 = request.POST.get('泡沫干粉联用消防车')
    sq.干粉消防车 = request.POST.get('干粉消防车')
    sq.云梯消防车 = request.POST.get('云梯消防车')
    sq.二氧化碳消防车 = request.POST.get('二氧化碳消防车')
    sq.save_eq = f
    sq.save()
    pq = Person_eq()
    pq.防护服 = request.POST.get('防护服')
    pq.足防护 = request.POST.get('足防护')
    pq.手防护 = request.POST.get('手防护')
    pq.头盔 = request.POST.get('头盔')
    pq.呼吸器 = request.POST.get('呼吸器')
    pq.per_eq = f
    pq.save()
    return HttpResponseRedirect('/fire/adminfight')


# 管理员删除作战指挥情况案例
def deletefight(request):
    id = request.GET.get('id')
    Fight_com.objects.get(id=id).delete()
    return HttpResponseRedirect('/fire/adminfight')

# 作战指挥情况详情:
def fightdetail(request):
    id = request.GET.get('id')
    username = request.session.get('name')
    f = Fight_com.objects.filter(id=id)
    fs = Fight_com.objects.get(id=id).fire_save_set.all()
    sq = Fight_com.objects.get(id=id).save_eq_set.all()
    pq = Fight_com.objects.get(id=id).person_eq_set.all()
    return render(request, 'fire/adminfile/fightdetail.html',
                  {'f1': f, 'fs1': fs, 'sq1': sq, 'pq1': pq, 'username': username})

# 作战指挥情况搜索函数
def adfgsearch(request):
    range1 = None
    range2 = None
    range3 = None
    lastButOne = 0
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    if request.method == 'POST':
        area = request.POST.get('area')
        if area == '':
            return HttpResponseRedirect('/fire/fight')
    else:
        area = request.GET.get('area')
        if area == '':
            return HttpResponseRedirect('/fire/fight')
    f1 = Fight_com.objects.filter(area__icontains=area)
    f = f1.values_list()
    # 一页十条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/adminfile/adfgsearch.html', {'Page': Page,
                                                              'ifEllipsis': ifEllipsis,
                                                              'range1': range1,
                                                              'range2': range2,
                                                              'range3': range3,
                                                              'lastButOne': lastButOne,
                                                              'area': area,
                                                              'user': user})


'''************************管理员管理经验总结函数************************'''


# 管理员跳转到经验总结函数:
def adminexper(request):
    range1 = None
    range2 = None
    range3 = None
    lastButOne = 0
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    e1 = Experience.objects.all()
    f = e1.values_list()
    # 一页十条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/adminfile/adminexper.html', {'Page': Page,
                                                              'ifEllipsis': ifEllipsis,
                                                              'range1': range1,
                                                              'range2': range2,
                                                              'range3': range3,
                                                              'lastButOne': lastButOne,
                                                              'user': user})


# 管理员更新经验总结情况界面
def updatee(request):
    username = request.session.get('name')
    id = request.GET.get('id')
    e = Experience.objects.filter(id=id)
    return render(request, 'fire/adminfile/updateexper.html', {'e1': e})


# 管理员更新经验总结情况案例
def updateexper(request):
    id = request.GET.get('id')
    e = Experience.objects.get(id=id)
    e.title = request.POST.get('title')
    e.place = request.POST.get('place')
    e.area = request.POST.get('area')
    e.fire_economic = request.POST.get('fire_economic')
    e.fire_cause = request.POST.get('fire_cause')
    e.fire_res = request.POST.get('fire_res')
    e.fire_exper = request.POST.get('fire_exper')
    e.fire_com = request.POST.get('fire_com')
    e.dis_mea = request.POST.get('dis_mea')
    e.dead.死亡人数 = request.POST.get('死亡人数')
    e.dead.重伤人数 = request.POST.get('重伤人数')
    e.dead.轻伤人数 = request.POST.get('轻伤人数')
    e.dead.男性死亡人数 = request.POST.get('男性死亡人数')
    e.dead.女性死亡人数 = request.POST.get('女性死亡人数')
    e.dead.本地死亡人数 = request.POST.get('本地死亡人数')
    e.dead.外地死亡人数 = request.POST.get('外地死亡人数')
    e.save()
    return HttpResponseRedirect('/fire/adminexper')


# 管理员增加经验总结情况案例界面
def alterexper1(request):
    return render(request, 'fire/adminfile/alterexper.html')


# 管理员增加经验总结情况案例
def alterexper(request):
    p = Person_hurt()
    p.死亡人数 = request.POST.get('死亡人数')
    p.重伤人数 = request.POST.get('重伤人数')
    p.轻伤人数 = request.POST.get('轻伤人数')
    p.男性死亡人数 = request.POST.get('男性死亡人数')
    p.女性死亡人数 = request.POST.get('女性死亡人数')
    p.本地死亡人数 = request.POST.get('本地死亡人数')
    p.外地死亡人数 = request.POST.get('外地死亡人数')
    p.dead_people1 = request.POST.get('dead1')
    p.dead_people2 = request.POST.get('dead2')
    p.dead_people3 = request.POST.get('dead3')
    p.save()
    e = Experience()
    e.title = request.POST.get('title')
    e.place = request.POST.get('place')
    e.area = request.POST.get('area')
    e.fire_economic = request.POST.get('fire_economic')
    e.fire_cause = request.POST.get('fire_cause')
    e.fire_res = request.POST.get('fire_res')
    e.fire_exper = request.POST.get('fire_exper')
    e.fire_com = request.POST.get('fire_com')
    e.dis_mea = request.POST.get('dis_mea')
    e.dead = p
    e.save()
    return HttpResponseRedirect('/fire/adminexper')


# 管理员删除经验总结案例
def deleteexper(request):
    id = request.GET.get('id')
    Experience.objects.get(id=id).delete()
    return HttpResponseRedirect('/fire/adminexper')

# 经验总结情况详情
def experdetail(request):
    id = request.GET.get('id')
    username = request.session.get('name')
    e = Experience.objects.filter(id=id)
    return render(request, 'fire/adminfile/experdetail.html', {'e1': e, 'username': username})

# 经验总结情况搜索函数
def adexsearch(request):
    range1 = None
    range2 = None
    range3 = None
    lastButOne = 0
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    if request.method == 'POST':
        title = request.POST.get('title')
        if type == '':
            return HttpResponseRedirect('/fire/firesi')
    else:
        title = request.GET.get('title')
        if type == '':
            return HttpResponseRedirect('/fire/firesi')
    f1 = Experience.objects.filter(title__icontains=title)
    f = f1.values_list()
    # 一页十条数据
    paginator = Paginator(f, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/adminfile/adexsearch.html', {'Page': Page,
                                                              'ifEllipsis': ifEllipsis,
                                                              'range1': range1,
                                                              'range2': range2,
                                                              'range3': range3,
                                                              'lastButOne': lastButOne,
                                                              'user': user,
                                                              'title': title})



# 用户查看火灾基本情况详情
def fireside(request):
    id = request.GET.get('id')
    username = request.session.get('name')
    f = Firesi.objects.filter(id=id)
    e = Firesi.objects.get(id=id).build_char_set.all()
    return render(request, 'fire/fireside.html', {'f1': f, 'e1': e, 'username': username})


# 用户查看作战指挥情况详情
def fightde(request):
    id = request.GET.get('id')
    username = request.session.get('name')
    f = Fight_com.objects.filter(id=id)
    fs = Fight_com.objects.get(id=id).fire_save_set.all()
    sq = Fight_com.objects.get(id=id).save_eq_set.all()
    pq = Fight_com.objects.get(id=id).person_eq_set.all()
    return render(request, 'fire/fightde.html', {'f1': f, 'fs1': fs, 'sq1': sq, 'pq1': pq, 'username': username})


# 用户查看经验总结情况情况详情
def experde(request):
    id = request.GET.get('id')
    username = request.session.get('name')
    e = Experience.objects.filter(id=id)
    return render(request, 'fire/experde.html', {'e1': e, 'username': username})


'''********************************************************'''

# /show_upload
def show_upload(request):
    '''显示上传图片'''
    return render(request, 'fire/upload_pic.html')


def upload_handle(request):
    '''上传图片处理'''
    # 1.获取上传文件处理对象
    pic = request.FILES['pic']
    # 2.创建文件
    save_path = '%s/fire/%s'%(settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        # 3.获取上传文件的内容并写到创建的文件中
        for content in pic.chunks():
            f.write(content)

    # 4.保存记录
    p =PicTest.objects.create(goods_pic='fire/%s'%pic.name)
    # 5.返回
    return render(request, 'fire/test.html', {'p': p})



'''************************爬虫模块************************'''
# 爬虫首页
def rep_index(request):
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    return render(request, 'fire/Reptile/rep_index.html', {'user': user})

# 火灾基本情况爬取界面
def rep_firesi(request):
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    return render(request,'fire/Reptile/rep_firesi.html', {'user': user})

# 作战指挥情况爬取界面
def rep_fight(request):
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    return render(request, 'fire/Reptile/rep_fight.html', {'user': user})

# 经验总结情况爬取界面
def rep_exper(request):
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    return render(request, 'fire/Reptile/rep_exper.html', {'user': user})



# 测试函数

def test(request):
    e1 = Firesi.objects.all()
    f = e1.values_list()
    # 一页十条数据
    paginator = Paginator(f, 10)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/test.html', {'Page': Page,
                                              'ifEllipsis': ifEllipsis,
                                              'range1': range1,
                                              'range2': range2,
                                              'range3': range3,
                                              'lastButOne': lastButOne})

# 救援方案管理开始

def ruleindex(request):
    # 救援方案
    index_form = forms.IndexForm
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    # 可视化
    return render(request, 'fire/rule/ruleindex.html', locals())

def adminruleindex(request):
    # 救援方案
    index_form = forms.IndexForm
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    # 可视化
    return render(request, 'fire/rule/adminruleindex.html', locals())

def ajax_sb(request):
    if request.method == 'GET':
        return render(request, 'fire/rule/ruleindex.html')
    elif request.method == 'POST':
        # 获取数据
        place = request.POST.get('place')
        print(place)
        area = int(request.POST.get('area'))
        volume = int(request.POST.get('volume'))
        call = int(request.POST.get('call'))
        stage = int(request.POST.get('stage'))
        fire = int(request.POST.get('fire'))
        speed = int(request.POST.get('speed'))
        trapped = int(request.POST.get('trapped'))
        injured = int(request.POST.get('injured'))
        death = int(request.POST.get('death'))
        # 火灾类别判断
        p = models.PlaceInfo.objects.get(id=place)
        print(p)
        c = p.Pcat_id
        print(c)
        cat = models.CategoryInfo.objects.get(id=c)
        ret = model_to_dict(cat)
        print(ret)
        cate = ret['Cgy']
        print(cate)
        # 火灾级别判断
        if area <= 100 or volume <= 1000 or call < 3 or stage == 1 or fire == 1 or speed == 1 or trapped == 0 or injured == 0 or death == 0:
            lev = '一级火灾'
            le = models.LevelInfo.objects.get(lev=lev)
            # 决策方案判断
            l = le.id
            de = models.DecisionInfo.objects.get(Pcat_id=c, Alev_id=l)
            d = model_to_dict(de)
            dec = d['programme']
            return JsonResponse({'cate': cate, 'lev': lev, 'dec': dec})
        elif 100 <= area <= 300 or 1000 <= volume <= 3000 or 3 <= call < 5 or stage == 1 or fire == 2 or speed == 2 or trapped < 5 or injured < 5 or death == 0:
            lev = '二级火灾'
            le = models.LevelInfo.objects.get(lev=lev)
            # 决策方案判断
            l = le.id
            de = models.DecisionInfo.objects.get(Pcat_id=c, Alev_id=l)
            d = model_to_dict(de)
            dec = d['programme']
            return JsonResponse({'cate': cate, 'lev': lev, 'dec': dec})
        elif 300 <= area <= 600 or 3000 <= volume <= 5000 or 3 <= call < 5 or stage == 2 or fire == 3 or speed == 3 or 5 <= trapped < 10 or 5 <= injured < 10 and death < 3:
            lev = '三级火灾'
            le = models.LevelInfo.objects.get(lev=lev)
            # 决策方案判断
            l = le.id
            de = models.DecisionInfo.objects.get(Pcat_id=c, Alev_id=l)
            d = model_to_dict(de)
            dec = d['programme']
            return JsonResponse({'cate': cate, 'lev': lev, 'dec': dec})
        elif 600 <= area <= 1000 or 5000 <= volume <= 10000 or call >= 5 or stage == 2 or fire == 4 or speed == 4 or 10 <= trapped < 15 or 10 <= injured < 20 and 3 <= death < 10:
            lev = '四级火灾'
            le = models.LevelInfo.objects.get(lev=lev)
            # 决策方案判断
            l = le.id
            de = models.DecisionInfo.objects.get(Pcat_id=c, Alev_id=l)
            d = model_to_dict(de)
            dec = d['programme']
            return JsonResponse({'cate': cate, 'lev': lev, 'dec': dec})
        elif area >= 1000 or volume >= 10000 or call >= 5 or stage == 2 or fire == 5 or speed == 4 or trapped >= 15 or injured >= 20 or death >= 10:
            lev = '五级火灾'
            le = models.LevelInfo.objects.get(lev=lev)
            # 决策方案判断
            l = le.id
            de = models.DecisionInfo.objects.get(Pcat_id=c, Alev_id=l)
            d = model_to_dict(de)
            dec = d['programme']
            return JsonResponse({'cate': cate, 'lev': lev, 'dec': dec})
        else:
            return render(request, 'fire/rule/ruleindex.html', locals())


def dec(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    # 方案增加form表
    add_form = forms.DecForm
    # 方案修改
    update_form = forms.UpdataDecForm
    # 导入数据库数据
    cat = models.CategoryInfo.objects.all()
    e1 = models.DecisionInfo.objects.all()
    place = models.PlaceInfo.objects.all()
    programme = e1.values_list()
    # 一页十条数据
    paginator = Paginator(programme, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/rule/dec.html', locals())

def admindec(request):
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    # 方案增加form表
    add_form = forms.DecForm
    # 方案修改
    update_form = forms.UpdataDecForm
    # 导入数据库数据
    cat = models.CategoryInfo.objects.all()
    e1 = models.DecisionInfo.objects.all()
    place = models.PlaceInfo.objects.all()
    programme = e1.values_list()
    # 一页十条数据
    paginator = Paginator(programme, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/rule/admindec.html', locals())


def decdelete(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    id1 = request.GET.get('id')
    obj = models.DecisionInfo.objects.get(id=id1)
    obj.delete()
    return HttpResponseRedirect("/fire/dec")


def decadd(request):
    if request.method == 'GET':
        add_form = forms.DecForm
        return render(request, 'fire/rule/dec.html', locals())
    add_form = forms.DecForm(data=request.POST)
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    if add_form.is_valid():
        l = models.LevelInfo()
        dlev = add_form.cleaned_data.get('lev')
        lid = models.LevelInfo.objects.get(lev=dlev)
        c = models.CategoryInfo()
        dcat = add_form.cleaned_data.get('cat')
        cid = models.LevelInfo.objects.get(lev=dcat)
        d = models.DecisionInfo()
        d.Alev = lid
        d.Pcat = cid
        d.programme = add_form.cleaned_data.get('programme')
        d.save()
        return redirect('/fire/dec')
    return render(request, 'fire/rule/dec.html', locals())


def decupdata(request):
    if request.method == 'GET':
        update_form = forms.UpdataDecForm
        return render(request, 'fire/rule/dec.html', locals())
    update_form = forms.UpdataDecForm(data=request.POST)
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    id = request.POST.get("upid")
    if update_form.is_valid():
        l = models.LevelInfo()
        dlev = update_form.cleaned_data.get('lev')
        lid = models.LevelInfo.objects.get(lev=dlev)
        c = models.CategoryInfo()
        dcat = update_form.cleaned_data.get('cat')
        cid = models.LevelInfo.objects.get(lev=dcat)
        d = models.DecisionInfo.objects.get(id=id)
        d.Alev = lid
        d.Pcat = cid
        d.programme = update_form.cleaned_data.get('programme')
        d.save()
        return redirect('/fire/dec')
    return render(request, 'fire/rule/dec.html', locals())


def lev(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    # 规则增加啊form表
    add_form = forms.AttFrom
    updata_form = forms.UpdateAttFrom
    # 导入数据库数据
    cat = models.CategoryInfo.objects.all()
    e1 = models.FireRuleInfo.objects.all().order_by('id')
    firemanage = e1.values_list()
    # 一页十条数据
    paginator = Paginator(firemanage, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/rule/lev.html', locals())

def adminlev(request):
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    # 规则增加啊form表
    add_form = forms.AttFrom
    updata_form = forms.UpdateAttFrom
    # 导入数据库数据
    cat = models.CategoryInfo.objects.all()
    e1 = models.FireRuleInfo.objects.all().order_by('id')
    firemanage = e1.values_list()
    # 一页十条数据
    paginator = Paginator(firemanage, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/rule/adminlev.html', locals())


def levdelete(request):
    id1 = request.GET.get('id')
    obj = models.FireRuleInfo.objects.get(id=id1)
    obj.delete()
    return HttpResponseRedirect("/fire/lev")


def levadd(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    cat = models.CategoryInfo.objects.all()
    firemanage = models.FireRuleInfo.objects.all()
    programme = models.DecisionInfo.objects.all()
    place = models.PlaceInfo.objects.all()
    if request.method == 'GET':
        add_form = forms.AttFrom
        return render(request, 'fire/rule/lev.html', locals())
    add_form = forms.AttFrom(request.POST)
    if add_form.is_valid():
        alev = request.POST.get('lev')
        lid = models.LevelInfo.objects.get(id=int(alev))
        a = models.FireRuleInfo()
        a.area = request.POST.get('area')
        a.volume = request.POST.get('volume')
        a.call = request.POST.get('call')
        a.stage = request.POST.get('stage')
        a.fire = request.POST.get('fire')
        a.speed = request.POST.get('speed')
        a.trapped = request.POST.get('trapped')
        a.injured = request.POST.get('injured')
        a.death = request.POST.get('death')
        a.Alev = lid
        a.save()
        massage = '添加成功!'
        return HttpResponse(massage)
    return render(request, 'fire/rule/lev.html', locals())


def levupdate(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    cat = models.CategoryInfo.objects.all()
    firemanage = models.FireRuleInfo.objects.all()
    programme = models.DecisionInfo.objects.all()
    place = models.PlaceInfo.objects.all()
    if request.method == 'GET':
        updata_form = forms.UpdateAttFrom
        return render(request, 'fire/rule/lev.html', locals())
    updata_form = forms.UpdateAttFrom(data=request.POST)
    id = request.POST.get("id")
    if updata_form.is_valid():
        l = models.LevelInfo()
        alev = updata_form.cleaned_data.get('lev')
        lid = models.LevelInfo.objects.get(lev=alev)
        a = models.FireRuleInfo.objects.get(id=id)
        a.area = updata_form.cleaned_data.get('area')
        a.volume = updata_form.cleaned_data.get('volume')
        a.call = updata_form.cleaned_data.get('call')
        a.stage = updata_form.cleaned_data.get('stage')
        a.fire = updata_form.cleaned_data.get('fire')
        a.speed = updata_form.cleaned_data.get('speed')
        a.trapped = updata_form.cleaned_data.get('trapped')
        a.injured = updata_form.cleaned_data.get('injured')
        a.death = updata_form.cleaned_data.get('death')
        a.Alev = lid
        a.save()
        return redirect('/fire/lev')
    return render(request, 'fire/rule/lev.html', locals())


def cat(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    # form表
    add_form = forms.CateFrom
    updata_form = forms.UpdateCateFrom
    # 导入数据库数据
    e1 = models.PlaceInfo.objects.all().order_by('id')
    firemanage = models.FireRuleInfo.objects.all().order_by('id')
    cat = e1.values_list()
    # 一页八条数据
    paginator = Paginator(cat, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/rule/cat.html', locals())

def admincat(request):
    username = request.session.get('name')
    user = Ad_Per.objects.filter(username=username)
    # form表
    add_form = forms.CateFrom
    updata_form = forms.UpdateCateFrom
    # 导入数据库数据
    e1 = models.PlaceInfo.objects.all().order_by('id')
    firemanage = models.FireRuleInfo.objects.all().order_by('id')
    cat = e1.values_list()
    # 一页八条数据
    paginator = Paginator(cat, 8)
    # 获取页码，默认第一页
    page_num = request.GET.get('page', '1')
    try:
        Page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):
        Page = paginator.page('1')
    # 这里是后端逻辑判断
    if Page.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = Page.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    return render(request, 'fire/rule/admincat.html', locals())


def catdelete(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    id1 = request.GET.get('id')
    obj = models.FireRuleInfo.objects.get(id=id1)
    obj.delete()
    return HttpResponseRedirect("/fire/cat")


def catadd(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    cat = models.CategoryInfo.objects.all()
    firemanage = models.FireRuleInfo.objects.all()
    programme = models.DecisionInfo.objects.all()
    place = models.PlaceInfo.objects.all()
    if request.method == 'GET':
        add_form = forms.CateFrom
        return render(request, 'fire/rule/cat.html', locals())
    add_form = forms.CateFrom(request.POST)
    if add_form.is_valid():
        pcat = request.POST.get('cat')
        cid = models.CategoryInfo.objects.get(id=int(pcat))
        a = models.PlaceInfo()
        a.address = request.POST.get('address')
        a.Pcat = cid
        a.save()
        massage = '添加成功!'
        return HttpResponse(massage)
    return render(request, 'fire/rule/cat.html', locals())

def catupdate(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    cat = models.CategoryInfo.objects.all()
    firemanage = models.FireRuleInfo.objects.all()
    programme = models.DecisionInfo.objects.all()
    place = models.PlaceInfo.objects.all()
    if request.method == 'GET':
        updata_form = forms.UpdateCateFrom
        return render(request, 'fire/rule/cat.html', locals())
    updata_form = forms.UpdateCateFrom(data=request.POST)
    id = request.POST.get("id")
    if updata_form.is_valid():
        c = models.CategoryInfo()
        pcat = updata_form.cleaned_data.get('cat')
        cid = models.CategoryInfo.objects.get(Cgy=pcat)
        a = models.PlaceInfo.objects.get(id=id)
        a.address = updata_form.cleaned_data.get('address')
        a.Pcat = cid
        a.save()
        return redirect('/fire/cat')
    return render(request, 'fire/rule/cat.html', locals())


def typevis(request):
    # 可视化
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    sql = "select * from t_fire"
    df = pd.read_sql_query(sql, ENGINE)
    df1 = df.loc[:, 'type'].value_counts()
    df2 = df.loc[:, 'level'].value_counts()
    df3 =df.loc[:, 'province'].value_counts()
    fire_time = df.loc[:, 'start_date']
    fire_time1 = fire_time.head(50)

    # 火灾类别与级别
    grid1_2 = Grid(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1300px", height="600px"))
    pie1 = (
        # 创捷饼图
        Pie(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
            .add("", list(zip(['A类', 'E类', 'B类', 'C类', 'D类'], df1)),
                 center=["20%", "50%"])  # 饼图中心的位置，即整个图的位置。格式：[左右，上下]

            .set_global_opts(title_opts=opts.TitleOpts(title="火灾类型", pos_left='5%'),
                             legend_opts=opts.LegendOpts(pos_left='5%', pos_bottom='0%'))

            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}\n({d}%)"))
    )
    pie2 = (
        # 创捷饼图
        Pie(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
            .add("", list(zip(['一般火灾', '较大火灾', '重大火灾', '未知'], df2)),
                 center=["65%", "50%"])  # 饼图中心的位置，即整个图的位置。格式：[左右，上下]

            .set_global_opts(title_opts=opts.TitleOpts(title="火灾级别", pos_right='40%'),
                             legend_opts=opts.LegendOpts(pos_right='20%', pos_bottom='0%'))

            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}\n({d}%)"))
    )
    # 将两个图表分别添加到grid对象里面去
    # 对grid的pos参数而言，pos_left是显示在靠右的位置 pos_right同理
    grid1_2.add(pie1, grid_opts=opts.GridOpts(pos_left="55%"))
    grid1_2.add(pie2, grid_opts=opts.GridOpts(pos_right="55%"))
    # page里可以add多种元素，grid chart image等等
    pic = grid1_2.render_embed()


    return render(request, 'fire/visionlize/typervis.html', locals())


def datevis(request):
    # 可视化
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    sql = "select * from t_fire"
    df = pd.read_sql_query(sql, ENGINE)
    df1 = df.loc[:, 'type'].value_counts()
    df2 = df.loc[:, 'level'].value_counts()
    df3 = df.loc[:, 'province'].value_counts()
    fire_time = df.loc[:, 'start_date']
    fire_time1 = fire_time.head(50)
    # 火灾日期数量统计
    plt.figure(figsize=(10, 10))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换sans-serif字体为SimHei
    plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号问题

    plt.hist(fire_time1, rwidth=0.8, bins=50, label="时间")  # rwidth条形图宽度，bins条形图个数，label图例名称
    plt.legend(fontsize=10)  # legend与label合用，有了legend才能显示label，fontsize调整其大小

    plt.xticks(rotation=90)  # 设置 X轴属性，rotation顺时针旋转
    plt.rcParams['xtick.labelsize'] = 10  # 设置X轴刻度大小
    plt.rcParams['ytick.labelsize'] = 10  # 设置y轴刻度大小

    plt.xlabel('日期', size=10)  # 设置X轴名称
    plt.ylabel('数量', size=10)
    plt.title('火灾日期数量统计图', size='15')
    plt.savefig('static\\img\\01.png')
    # plt.show()

    grid1_1 = Grid(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1350px", height="600px"))
    bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    bar.add_xaxis(fire_time1)
    bar.add_yaxis('数量', fire_time1)
    bar.set_global_opts(title_opts=opts.TitleOpts(title='火灾日期数量'))
    tm = bar.render_embed()
    return render(request, 'fire/visionlize/datevis.html', locals())


def pronvis(request):
    username = request.session.get('name')
    user = Person.objects.filter(username=username)
    sql = "select * from t_fire"
    df = pd.read_sql_query(sql, ENGINE)
    df1 = df.loc[:, 'type'].value_counts()
    df2 = df.loc[:, 'level'].value_counts()
    df3 = df.loc[:, 'province'].value_counts()
    fire_time = df.loc[:, 'start_date']
    fire_time1 = fire_time.head(50)
    grid1_3 = Grid(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1350px", height="800px"))
    pie3 = (
        # 创捷饼图
        Pie(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
            .add("", list(zip(['福建省', '广东省', '浙江省', '江苏省', '湖北省', '广西壮族自治区', '湖南省', '山东省', '上海市'
                                  , '四川省', '山西省', '内蒙古自治区', '湖北省', '陕西省', '河北省', '新疆维吾尔自治区'
                                  , '河南省', '安徽省', '辽宁省', '云南省', '贵州省', '重庆市', '江西省', '黑龙江省', '海南省'
                                  , '青海省', '吉林省', '北京市', '甘肃省', '宁夏回族自治区', '未知', '天津市', '西安省'], df3)),
                 center=["50%", "40%"])  # 饼图中心的位置，即整个图的位置。格式：[左右，上下]

            .set_global_opts(title_opts=opts.TitleOpts(title="所属省份", pos_left='7%', pos_top='5%'),
                             legend_opts=opts.LegendOpts(pos_right='5%', pos_bottom='0%'))

            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}\n({d}%)"))
    )
    grid1_3.add(pie3, grid_opts=opts.GridOpts(pos_left="55%"))
    pr = grid1_3.render_embed()
    return render(request, 'fire/visionlize/pronvis.html', locals())