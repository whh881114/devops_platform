# -*- coding: utf-8 -*-

from rest_framework import exceptions
class SessionIDAuth(object):
    def authenticate(self, request):
        # 将原生的request.user对象返回，以方便后续的permission进行判断。
        user = request._request.user

        # print('-' * 20 + 'SessionIDAuth' + '-' * 20)
        # print(str(request._request.user))
        # print(request._request.user.is_superuser)
        # print('-' * 20 + 'SessionIDAuth' + '-' * 20)

        if str(request._request.user) == 'AnonymousUser':
            raise exceptions.AuthenticationFailed('Authentication failed.')
        return (user, None)


    def authenticate_header(self, request):
        pass