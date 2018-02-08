from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.db import connection
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import *
import time
import datetime
import random
import os
import json


def error(request):
    return render(request,"404.html");
# 生成随机数
def randomString():
    for i in range(1,10):
        now_time=datetime.datetime.now().strftime("%Y%m%d%H%M%S");
        randomNum=random.randint(1,100);
        if randomNum < 0:
            randomNum=str(0)+str(randomNum);
        randomNumId=str(now_time) + str(randomNum);
    return randomNumId
# Create your views here.
def home(request):
    return render(request,"personbase.html")
def login(request):
    return render(request,"login.html")
# 用户登录接口
def loginApi(request):
    print("+++++++++++++++++++++++++++")
    name=request.POST["username"];
    pwd=request.POST["pwd"]; 
    cursor=connection.cursor();
    sql="select * from user where username ='%s' and password = '%s' "%(name,pwd);
    cursor.execute(sql);
    a=cursor.fetchall();
    print("-------------",a)
    if a:
        return HttpResponse(json.dumps({'status':'ok'}),content_type="application/json");
    else:
        return HttpResponse(json.dumps({'status':'error'}),content_type="application/json");
    print(name,pwd)
    cursor.close()
    return HttpResponse("******************************")


#main页面请求
def main_show(request):
    return render(request,"main.html")

#main页面数据图片显示
def main_showApi(request):
    sql="select * from project"
    cursor=connection.cursor();
    cursor.execute(sql);
    allprojectTable=[]
    for row in cursor.fetchall():
        projectTable={
            'projectid':row[0],
            'projectname':row[1],
            'propicture':row[2],
            'prodetail':row[3],
            'proteacher':row[4],
        }
        allprojectTable.append(projectTable)
    cursor.close();
    return HttpResponse(json.dumps({'data':allprojectTable,'status':'ok'}),content_type="application/json")
#注册接口
def registerApi(request):
    name=str(request.POST["username"]);
    pwd=str(request.POST["pwd"]);
    userid=randomString()
    userid=str(userid)
    print(type(userid));
    print(type(name));
    print(type(pwd));
    print(name,pwd,userid)
    cursor=connection.cursor();
    sql="insert into user (userid,username,password) values ('%s','%s','%s')" %(userid,name,pwd);
    cursor.execute(sql)
    print("******************************************")
    return HttpResponse(json.dumps({'status':'ok'}),content_type="application/json")
#课程添加
def sss(request):
    return render(request,"ttt.html")

    

# 后台课程添加接口
def projectAdd(request):
     # img=request.FILES["imgfile"]
    projectid=randomString();
    projectname=request.POST["projectname"];
    propicture=request.FILES["propicture"];
    prodetail=request.POST["prodetail"]
    proteacher=request.POST["proteacher"]
    charptertitle=request.POST["charptertitle"]
    charpter=request.POST["charpter"]
    charptercontent=request.POST["charptercontent"]
    propicturename=randomString()+".jpg";
    filepath = "./project/static/myfile/";
    filename=os.path.join(filepath,propicturename);
    filename=open(filename,'wb')
    filename.write(propicture.__dict__["file"].read());
    cursor=connection.cursor();
    sql="insert into project(projectid,projectname,propicture,prodetail,proteacher,charptertitle,charpter,charptercontent) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"%(projectid,projectname,propicturename,prodetail,proteacher,charptertitle,charpter,charptercontent);
    cursor.execute(sql);
    print(projectname,propicturename,prodetail)
    return HttpResponse("dddddddddddd")
def base(request):
    return render(request,"personbase.html")
#我的主页展示界面
def mymain(request):
    return render(request,"mymain.html")

#联系我们展现界面
def mail(request):
    return render(request,"mail.html")
# 联系我们接口
def mailApi(request):
    print("++++++++++++++++")
    name=request.POST["name"];
    phone=request.POST["phonenumber"]
    advice=request.POST["advice"]
    cursor=connection.cursor();
    sql="insert into advice(name,phone,content) values('%s','%s','%s')"%(name,phone,advice);
    cursor.execute(sql)
    return HttpResponse(json.dumps({'status':'ok'}),content_type="application/json")

#我的课程展示接口
def myproject(request):
    return render(request,"myproject.html")
def myprojectApi(request):
    print("ddddddddddd");
    for key in request.POST:
        userid = request.POST.getlist(key)[0];
    print(userid);
    cursor=connection.cursor();
    sql="select * from project where userid = '%s'" % userid;
    cursor.execute(sql);
    a=cursor.fetchall();
    allMyproject=[];
    for row in a:
        myproject={
            'projectid':row[0],
            'projectname':row[1],
            'propicture':row[2],
            'prodetail':row[3],
            'proteacher':row[4],
        }
        allMyproject.append(myproject);
    print(allMyproject)
    cursor.close();
    return HttpResponse(json.dumps({"data":allMyproject}),content_type="application/json")

#信息修改接口
def updateApi(request):
    userid = request.POST["userid"];
    password=request.POST["password"];
    phone=request.POST["phone"];
    if password!="" and phone!="":
        sql="update user set password = '%s',telnumber = '%s' where username = '%s'"%(password,phone,userid)
    elif password=="" and phone!="":
        sql="update user set telnumber = '%s' where username = '%s'"%(phone,userid)
    elif password!="" and phone=="":
        sql="update user set password = '%s' where username = '%s'"%(password,userid)
        
    else:
        return HttpResponse(json.dumps({'status':'error'}),content_type="application/json")
    cursor=connection.cursor();
    cursor.execute(sql);
    cursor.close()
    print("*******************************")
    return HttpResponse(json.dumps({'status':'ok'}),content_type="application/json")

#信息修改界面展示
def update(request):
    return render(request,"update.html")

# 添加课程数据请求接口
def addprojectApi(request):
    sql="select * from project";
    cursor=connection.cursor();
    cursor.execute(sql);
    allprojectTable=[]
    for row in cursor.fetchall():
        projecttable={
            'projectid':row[0],
            'projectname':row[1],
            'propicture':row[2],
            'proteacher':row[4],
            'charpertitle':row[5],
        }
        allprojectTable.append(projecttable);
    cursor.close();
    return HttpResponse(json.dumps({'data':allprojectTable,'status':'ok'}),content_type="application/json")

#添加课程界面展示接口
def addproject(request):
    return render(request,"addproject.html")
#用户课程添加接口
def personprojectAdd(request):
    return HttpResponse("ooooooooooooooooooo")

#详细课程展示界面
def projectdetail(request):
    return render(request,"projectdetail.html")

#详细信息展示页面接口
def projectdetailApi(request):
    return HttpResponse("我是详细信息展示页面接口")