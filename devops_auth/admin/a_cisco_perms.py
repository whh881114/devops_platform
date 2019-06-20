# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..models.m_cisco_perms import CiscoPerms


# Register your models here.
class CiscoPermsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'userid_id',
        'read',
        'write',
        'execute',
    ]
    list_filter = ['userid_id']
    list_per_page = 10
admin.site.register(CiscoPerms, CiscoPermsAdmin)