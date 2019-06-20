# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import logout



class LogoutView(APIView):
    def get(self,request):
        '''
        前后端分离，认证成功后，客户端每次请求时Cookie中携带了sessionid，logout()则通过sessionid删除数据库中对应的记录。
        :param request:
        :return:
        '''
        logout(request)
        ret_code = {'code': 0, 'msg': 'User logout successfully.'}
        return JsonResponse(ret_code)