from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from .models import ProfileMd

class ProfileFm(ModelForm):

  class Meta:
    model = ProfileMd
    fields = [
      'sex',
      'address',
      'civil_state',
      'ocupation',
    ]
    labels = {
      'sex': 'Sex',
      'address': 'Address',
      'civil_state': 'Civil State',
      'ocupation': 'Ocupation',
    }
    widgets = {
      'sex': TextInput(attrs={'type':'text', 'max_length':'1'}),
      'address': TextInput(attrs={'type':'text', 'max_length':'64'}),
      'civil_state': TextInput(attrs={'type':'text', 'max_length':'1'}),
      'ocupation': TextInput(attrs={'type':'text', 'max_length':'64'}),
    }
    help_text = {
      'sex': 'M:Male, F:Female',
      'address': 'Full address',
      'civil_state': 'S:single, M:married, D:divorced, W:widowed',
      'ocupation': 'Student, Worker, Employer, Unoccupied, etc',
    }

class UserFm(ModelForm):

  class Meta:
    model = User
    fields = [
      'username',
      'email',
      'first_name',
      'last_name',
    ]
    labels = {
      'username': 'User name',
      'email': 'Email',
      'first_name': 'First name',
      'last_name': 'Last name',
    }
    widgets = {
      'username': TextInput(attrs={'type':'text', 'max_length':'64'}),
      'email': TextInput(attrs={'type':'email', 'max_length':'64'}),
      'first_name': TextInput(attrs={'type':'text', 'max_length':'64'}),
      'last_name': TextInput(attrs={'type':'text', 'max_length':'64'}),
    }