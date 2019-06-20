# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User


class AuthView(APIView):
    def get(self, request):
        '''
        前后端分离，验证sessionid是否合法，即验证用户是否已登录。
        :param request:
        :return:
        '''
        from django.contrib.sessions.models import Session
        sessionid = request.session.session_key

        if sessionid is not None:
            ret = Session.objects.filter(session_key=sessionid)
            username = str(request.user)
            userid = request.user.id
            user_is_superuser = User.objects.all().filter(id=userid).values()[0]['is_superuser']
            print(user_is_superuser)

            if len(ret) != 0:
                ret_code = {'code': 0,
                            'username': username,
                            'userid': userid,
                            'user_is_superuser': user_is_superuser,
                            'msg': 'User has logged in.'}
                return JsonResponse(ret_code)
        else:
            ret_code = {'code': 1,
                        'msg': 'User has not logged in.'}
            return JsonResponse(ret_code, status=401)