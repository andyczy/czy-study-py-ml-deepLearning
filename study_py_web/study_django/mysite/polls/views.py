from django.shortcuts import render

# 视图层
# Create your views here.
from django.http import HttpResponse
from . import models

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # sqlLite
    # user = models.User.objects.get(pk=1)
    users = models.User.objects.all()
    return render(request,"index.html",{"key":"this is key-value","users":users})


def userById(request,userById):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # sqlLite
    user = models.User.objects.get(pk=userById)
    return render(request,"index.html",{"key":"this is key-value","user":user})



def edit(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # sqlLite
    # name = request.POST.get("name","测试添加")
    a = models.User.objects.create(userName="测试添加",title="测试标题")
    print("===",a)
    users = models.User.objects.all()

    user = models.User.objects.get(pk=4)
    user.title = "修改标题"
    user.userName = "修改名字"
    user.save()
    return render(request,"index.html",{"key":"this is key-value","users":users})






