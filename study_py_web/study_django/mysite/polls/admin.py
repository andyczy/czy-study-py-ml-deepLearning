from django.contrib import admin

# 当前自带的后台管理系统
# Register your models here.
from .models import User

admin.site.register(User)