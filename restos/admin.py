# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Resto
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your Resto here.
admin.site.register(Resto)
