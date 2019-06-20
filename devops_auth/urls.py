# -*- coding: utf-8 -*-
"""devops_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from views.v_auth import AuthView
from views.v_login import LoginView
from views.v_logout import LogoutView
from views.v_modify_passwd import ModifyPasswdView
from views.v_get_perms import GetPermsView


urlpatterns = [
    # 用于判断用户是否已通过用户名和密码成功登录网站。
    url(r'^is_auth/$', csrf_exempt(AuthView.as_view()), name='auth'),

    url(r'^login/$', csrf_exempt(LoginView.as_view()), name='login'),
    url(r'^logout/$', csrf_exempt(LogoutView.as_view()), name='logout'),

    # 用于用户修改初始化密码接口。
    url(r'^modify_password/$', csrf_exempt(ModifyPasswdView.as_view()), name='modify_password'),

    # 用于查询当前用户权限接口。
    url(r'^get_perms/$', csrf_exempt(GetPermsView.as_view()), name='get_perms'),
]
