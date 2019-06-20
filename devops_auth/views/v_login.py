# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login


# Create your views here.
class LoginView(APIView):
    def post(self, request):
        '''
        前后端分离，使用django自带的authenticate认证，认证成功后调用login()，将sessionid写入数据库。
        :param request:
        :return:
        '''
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # 开始判断初始是否有没更改，如果更改了，可以正常登录平台。如果没改，返回code为2，需要客户修改密码。
            original_password = username + "123456"
            # print('-' * 50)
            # print("password = %s" % password)
            # print("original_password = %s" % original_password)
            # print('-' * 50)
            if password != original_password:
                ret_code = {'code': 0, 'msg': 'User login successfully.'}
                return JsonResponse(ret_code)
            else:
                request.session.flush()
                ret_code = {'code': 2, 'msg': 'Please change password first.'}
                return JsonResponse(ret_code)
        else:
            ret_code = {'code': 1, 'msg': 'Invalid username or password, please check.'}
            return JsonResponse(ret_code)