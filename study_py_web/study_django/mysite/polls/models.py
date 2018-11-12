from django.db import models

# 数据模型（orm）
# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True,max_length=32)
    userName = models.CharField(max_length=32)