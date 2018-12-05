# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
import inspect

from django.contrib   import admin
from django.db.models import Model

import models


for n, c in inspect.getmembers(models):
  if inspect.isclass(c) and issubclass(c, Model):
    admin.site.register(c)

