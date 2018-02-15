# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Resto(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(default='')
    picture = models.CharField(max_length=1000, blank=True, default='')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name
