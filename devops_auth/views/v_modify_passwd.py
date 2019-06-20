# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import *


class ModifyPasswdView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        old_password = data['old_password']
        new_password = data['new_password']
        user = authenticate(request, username=username, password=old_password)
        # print('-' * 50)
        # print(type(user), user)
        # print('-' * 50)
        if user is not None:
            # 对新密码进行验证，如果合法，返回结果是None，就执行修改密码。
            if validate_password(new_password) is None:
                try:
                    user.set_password(new_password)
                    user.save()
                except:
                    ret_code = {'code': 1, 'msg': 'Password has not been modified.'}
                    return JsonResponse(ret_code)

                # 修改成功后，返回此状态。
                ret_code = {'code': 0, 'msg': 'Password has been modified successfully.'}
                return JsonResponse(ret_code)
        else:
            ret_code = {'code': 2, 'msg': 'Original password is incorrect, please check.'}
            return JsonResponse(ret_code)