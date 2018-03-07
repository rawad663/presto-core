# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    isResto = models.BooleanField('resto status', default=False)



class Resto(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(default='')
    #picture = 

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name
