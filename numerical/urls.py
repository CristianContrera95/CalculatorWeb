from django.conf.urls import url
from .views import RootsView, ResultView

app_name = 'numerical'
urlpatterns = [
  url(r'^roots$', RootsView.as_view(), name='roots'),
  url(r'^result$', ResultView.as_view(), name='result')
]