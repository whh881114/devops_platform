# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class HostPerms(models.Model):
    '''
    用户访问权限
    '''
    userid = models.OneToOneField(User, unique=True)

    read = models.BooleanField(default=True)
    write = models.BooleanField(default=False)
    execute = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.userid)