# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import *
from django.contrib.auth.models import User

from ..models.m_cisco_perms import CiscoPerms
from ..models.m_h3c_perms import H3cPerms
from ..models.m_helpdesk_perms import HelpdeskPerms
from ..models.m_host_perms import HostPerms
from ..models.m_mysql_perms import MysqlPerms
from ..models.m_oracle_perms import OraclePerms


class GetPermsView(APIView):
    def get(self, request):
        ret = {"perms": {}}


        # 根据用户来取对应的权限，如果是管理员，那么拥有所有权限，如果是匿名者则没有任何权限，一般用户则按后台设置的权限处理各种逻辑。
        # 根据user_role来判断用户角色。
        # 1. 当user_role为AnonymousUser时，不用判断perms的值，直接把所有权限设置为False。
        # 2. 当user_role为Administrator时，不用判断perms的值，直接把所有权限设置为True。
        # 3. 当user_role为GeneralUser时，权限请根据perms值来处理各个逻辑。

        username = str(request.user)
        # print('username=%s' % username)

        if username == 'AnonymousUser':
            user_role = {"user_role": "AnonymousUser"}
            ret.update(user_role)
        else:
            userid = request.user.id
            user_is_superuser = User.objects.all().filter(id=userid).values()[0]['is_superuser']

            if user_is_superuser is True:
                user_role = {"user_role": "Administrator"}
                ret.update(user_role)
            else:
                user_role = {"user_role": "GeneralUser"}
                ret.update(user_role)

                for perm in CiscoPerms, H3cPerms, HelpdeskPerms, HostPerms, MysqlPerms, OraclePerms:
                    perm_table_name = perm.__name__
                    my_perm = {perm_table_name: []}

                    if len(perm.objects.filter(userid_id=userid).values()) == 0:
                        my_perm[perm_table_name].append(False)
                        my_perm[perm_table_name].append(False)
                        my_perm[perm_table_name].append(False)
                    else:
                        my_perm[perm_table_name].append(perm.objects.filter(userid_id=userid).values()[0]['read'])
                        my_perm[perm_table_name].append(perm.objects.filter(userid_id=userid).values()[0]['write'])
                        my_perm[perm_table_name].append(perm.objects.filter(userid_id=userid).values()[0]['execute'])

                    ret['perms'].update(my_perm)

        return JsonResponse(ret, safe=False)

