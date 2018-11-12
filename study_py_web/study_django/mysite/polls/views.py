from django.shortcuts import render

# 视图层
# Create your views here.
from django.http import HttpResponse
from . import models

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # sqlLite
    user = models.User.objects.get(pk=1)
    return render(request,"index.html",{"key":"this is key-value","user":user})