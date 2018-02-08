"""SelectProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from project.views import *

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^home/',home),
    url(r'^registerApi/',registerApi),#注册接口
    url(r'^mainshow/',main_show),#主页面展现信息
    url(r'^mainshowApi/',main_showApi),#主页面展现信息接口
    url(r'^loginApi/',loginApi),#用户登录页面请求端口

    url(r'^myproject/',myproject),#我的课程展示接口
    url(r'^myprojectApi/',myprojectApi),#我的课程数据请求接口
    url(r'^updateApi/',updateApi),#信息修改接口
    url(r'^update/',update),#信息修改界面展示   
    
    
    url(r'^projectdetail/',projectdetail),#详细信息展示界面
    url(r'^projectdetailApi/',projectdetailApi),#详细信息展示界面接口

    url(r'^sss',sss),
    url(r'^addprojectApi/',addprojectApi),#添加课程数据请求接口
    url(r'^addproject/',addproject),#添加课程界面展示
    url(r'^projectAdd/',projectAdd),#课程数据添加接口
    url(r'^personprojectAdd/',personprojectAdd),#用户个人课程添加接口
    
    url(r'^base',base),
    url(r'^mymain/',mymain),#我的主页展示
    url(r'^mailApi/$',mailApi),#意见栏添加接口
    url(r'^mail/',mail),#意见栏展示界面
    
    url(r'^$',login),#用户登录页面端口
    url(r'^.',error),#错误界面

]
