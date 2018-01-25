# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (ListView, DeleteView, 
  RedirectView, TemplateView)
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import HistoryMd
from math import *


BASIC_OP = '+-*/()'


@method_decorator(require_http_methods(['GET']), name='dispatch')
class IndexView(ListView):
  template_name = 'calculator/index_tmp.html'
  context_object_name = 'ind_context'
  pk_url_kwarg = 'user_id'

  def get_context_data(self, *args, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    return context

  def get_queryset(self, **kwargs):
    ind_queryset = User.objects.order_by('-last_login')[:5]
    return ind_queryset


@method_decorator(login_required, name='dispatch')
class CalculatorView(TemplateView):
  template_name = 'calculator/calculator_tmp.html'
  context_object_name = 'cal_context'
  pk_url_kwarg = 'user_id'

  def get(self, request, *args, **kwargs):
    context = {
      'user': User.objects.get(id=self.kwargs.get('user_id')),
      'equation': '0',
      'result': '0',
    }
    return render(request, self.template_name, context)

  def make_equation(self, request):
    new_equation = '0'
    result = '0'

    equation = request.POST.get('equation')
    if equation != '0' and equation is not None:
      new_equation = equation
    digit = request.POST.get('digit')
    if digit:
      new_equation = new_equation + digit
    op = request.POST.get('op')
    if op and op in BASIC_OP:
      new_equation = new_equation + op
    equals = request.POST.get('equals')
    if equals:
      try:
        result = str(eval(equation))
      except SyntaxError, TypeError:
        result = 'Equation bad formed'
      except ValueError:
        result = 'NaN'
    return (new_equation, result)

  def post(self, request, *args, **kwargs):
    user = User.objects.get(id=self.kwargs.get('user_id'))

    (new_equation, result) = self.make_equation(request)
    if result != '0':
      user.historymd_set.create(user=user, count=user.historymd_set.count()+1,
                                equation=new_equation)
    context = { 
      'calculator_type' : True,
      'user': user,
      'new_equation': new_equation,
      'result': result, 
    }
    return render(request, self.template_name, context)



@method_decorator(login_required, name='dispatch')
class HistoryView(ListView):
  model = HistoryMd
  template_name = 'calculator/history_tmp.html'
  context_object_name = 'his_context'
  pk_url_kwarg = 'user_id'

  def get_context_data(self, *args, **kwargs):
    context = super(HistoryView, self).get_context_data(**kwargs)
    return context

  def get_queryset(self, **kwargs):
    user = User.objects.get(id=self.kwargs.get('user_id'))
    his_queryset = HistoryMd.objects.filter(user=user)
    return his_queryset




class GetResultView(RedirectView):
  pass