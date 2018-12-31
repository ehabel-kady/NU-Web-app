# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course (models.Model):
    title=models.CharField(max_length=200)
    code=models.CharField(max_length=200)
    creditHours=models.IntegerField()

    def __str__(self):
        return self.title