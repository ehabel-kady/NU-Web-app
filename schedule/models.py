# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class course_time(models.Model):
    code = models.CharField(max_length=200)
    room = models.CharField(max_length=50)
    time = models.CharField(max_length=200)
    def __str__(self):
        return self.room