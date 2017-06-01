# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Score(models.Model):
    """STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )"""
    username = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
