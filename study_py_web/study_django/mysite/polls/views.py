from django.shortcuts import render

# 视图层
# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,"index.html",{"key":"this is key-value"})