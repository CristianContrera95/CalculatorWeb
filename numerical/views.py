# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from .octave import roots

class RootsView(TemplateView):
  template_name = 'numerical/numerical_tmp.html'
  parameters = {
    'bisection':['function', 'a', 'b', 'tol', 'iter'],
    'newton':['function', 'Function\'', 'x0','tol', 'iter'],
    'ipf':['function', 'x0', 'tol', 'iter'],
  }
  def post(self, request):
    meth = request.POST.get('opcMethod')
    if meth:
      context = {
        'method': True,
        'meth': meth,
        'parameters': self.parameters[meth][1:],
      }
      return render(request, self.template_name, context=context)

    method = request.POST.get('selMethod')
    print method
    param = []
    for i in range(len(self.parameters[method])):
      param.append(request.POST.get(self.parameters[method][i]))
    result = roots(method, param)
    if result is None:
      result = [['Fail','']]
    context = {
      'result':result[0],
    }
    return render(request, 'numerical/result_tmp.html', context=context)

  def get(self, request):
    context = {
      'method': None,
    }
    return render(request, self.template_name, context=context)


class ResultView(TemplateView):
  pass