from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse


# Create your views here.

def logout_view(request):
    """退出登录"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
