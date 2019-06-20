# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..models.m_h3c_perms import H3cPerms


# Register your models here.
class H3cPermsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'userid_id',
        'read',
        'write',
        'execute',
    ]
    list_filter = ['userid_id']
    list_per_page = 10
admin.site.register(H3cPerms, H3cPermsAdmin)