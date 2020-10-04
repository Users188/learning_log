"""为应用程序users定义url模式"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns =[
    #登录页面
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login')

]