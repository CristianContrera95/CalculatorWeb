from django.forms import TextInput

from .models import RootsMd

class RootsFm(ModelForm):
  class Meta:
    model = RootsMd
    fields = [
      ]
