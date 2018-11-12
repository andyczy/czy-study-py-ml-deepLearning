from django.conf.urls import url

from . import views

urlpatterns = [
    # 空字符串
    url(r'^$', views.index, name='index'),
]
