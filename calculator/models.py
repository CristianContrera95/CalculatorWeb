# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models as md
from django.utils import timezone
from django.contrib.auth.models import User


class HistoryMd(md.Model):
  """docstring for HistoryMd"""
  user = md.ForeignKey(User, on_delete=md.CASCADE)
  count = md.IntegerField()
  equation = md.CharField(max_length=31, null=False)

  def __str__(self):
    return str(str(self.count)+': '+self.equation)

  class Meta:
    ordering = ('user','count',)