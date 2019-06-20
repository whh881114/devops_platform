# -*- coding: utf-8 -*-


from rest_framework.permissions import BasePermission
from ..models.m_h3c_perms import H3cPerms as M_H3cPerms


class H3cPerms(BasePermission):
    def has_permission(self, request, view):
        # print('-' * 50 + 'has_view_permission' + '-' * 50)
        if request.user.is_superuser:
            return True
        else:
            user_id = request.user.id
            # print('-' * 50)
            # print(user_id)
            perms = M_H3cPerms.objects.all().filter(userid_id=user_id).values('read', 'write', 'execute')[0]
            # print(perms)
            # print(request.method)

            if perms['read'] and request.method in ['GET']:
                return True

            elif perms['write'] and request.method in ['POST', 'PUT']:
                return True

            elif perms['execute'] and request.method in ['DELETE']:
                return True

            else:
                return False