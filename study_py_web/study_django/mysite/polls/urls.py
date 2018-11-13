from django.conf.urls import url

from . import views

urlpatterns = [
    # 空字符串
    url(r'^$', views.index, name='index'),
    url(r'^userById/(?P<userById>[0-9]+)$', views.userById, name='userById'),
    url(r'^edit$', views.edit, name='edit'),
]
