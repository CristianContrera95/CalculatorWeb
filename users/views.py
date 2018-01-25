# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import RedirectView, TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy

from .models import ProfileMd
from .forms import ProfileFm, UserFm


class LoginView(TemplateView):
  template_name = 'users/login_tmp.html'
  context_object_name = 'log_context'

  def post(self, request, *args, **kwargs):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      print 'user'
      login(request, user)
      return redirect('index/')
    else:
      log_context = {
        'error_msj': 'Invalid user',
      }
      return render(request, self.template_name, context=log_context)

  def get(self, request, *args, **kwargs):
    return render(request, self.template_name)



def logoutView(request):
  logout(request)
  return redirect('index/')


class RegisterView(CreateView):
  model = ProfileFm
  form_class = ProfileFm
  second_form_class = UserFm
  context_object_name = 'reg_context'
  template_name = 'users/register_tmp.html'
  success_url = reverse_lazy('users:index')

  def get_context_data(self, *args, **kwargs):
    reg_context = super(RegisterView, self).get_context_data(**kwargs)
    if 'form' not in reg_context:
      reg_context['form'] = self.form_class(self.request.GET)
    if 'form2' not in reg_context:
      reg_context['form2'] = self.second_form_class(self.request.GET)
    return reg_context

  def post(self, request, *args, **kwargs):
    error_reg = None
    self.object = self.get_object
    form = self.form_class(request.POST)
    form2 = self.second_form_class(request.POST)
    if form.is_valid() and form2.is_valid():
      password = request.POST.get('password2')
      if password == form2.cleaned_data['password']:
        profile = form.save(commit=False) #wait save a form2 save
        profile.user = form2.save()
        profile.save()
        return redirect(self.success_url)
      error_reg = 'Passwords are no equals'
    else:
      error_reg = 'Data Error'

    reg_context = self.get_context_data(form=form, form2=form2)
    reg_context['error_reg'] = error_reg
    return render(request, self.template_name, reg_context)


def auth(request):
  pass


class IndexView(TemplateView):
  template_name = 'users/index_tmp.html'


def profile(request):
  pass

