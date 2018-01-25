# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models as md
from django.contrib.auth.models import User


class ProfileMd(md.Model):
  user = md.OneToOneField(User, on_delete=md.CASCADE, primary_key=True)
  sex = md.CharField(max_length=1)
  address = md.CharField(max_length=64)
  civil_state = md.CharField(max_length=1)
  ocupation = md.CharField(max_length=64)

  def __str__(self):
    return (self.user.first_name+' '+self.user.last_name)

