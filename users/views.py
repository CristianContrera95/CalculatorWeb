# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.edit import  FormView
from django.views.generic.detail import  DetailView
from django.core.urlresolvers import reverse_lazy

from .models import ProfileMd
from .forms import ProfileFm, UserFm


def logoutView(request):
  logout(request)
  return redirect('index/')


class LoginView(TemplateView):
  template_name = 'users/login_tmp.html'
  context_object_name = 'log_context'

  def post(self, request, *args, **kwargs):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('index/')
    else:
      log_context = {
        'error_msj': 'Invalid user',
      }
      return render(request, self.template_name, context=log_context)


class RegisterView(FormView):
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
    form_prof = ProfileFm(request.POST)
    form_user = UserFm(request.POST)
    if form_prof.is_valid() and form_user.is_valid():
      password = request.POST.get('password')
      if password == request.POST.get('password2'):
        profile = form_prof.save(commit=False)
        user = form_user.save()
        user.set_password(password)
        profile.user = user
        user.save()
        profile.save()
        return redirect(self.success_url)
      error_reg = 'Passwords are no equals'
    else:
      error_reg = 'Data Error'

    reg_context = self.get_context_data(form=form_prof, form2=form_user)
    reg_context['error_reg'] = error_reg
    return render(request, self.template_name, reg_context)

  
class IndexView(TemplateView):
  template_name = 'users/index_tmp.html'


class ProfileView(DetailView):
  model = ProfileMd
  template_name = 'users/profile_tmp.html'
  context_object_name = 'pro_context'


