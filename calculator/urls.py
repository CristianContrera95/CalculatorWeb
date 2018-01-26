from django.conf.urls import url
from .views import HistoryView, CalculatorView, IndexView, GetResultView

app_name = 'calculator'

urlpatterns = [
  url(r'^$', IndexView.as_view(), name='index'),
  url(r'^calculator/(?P<pk>[0-9]+)/$', CalculatorView.as_view(), name='calculator'),
  url(r'^history/(?P<pk>[0-9]+)/$', HistoryView.as_view(), name='history'),
  url(r'^result/(?P<pk>[0-9]+)/$', GetResultView.as_view(), name='result'),

]