from django.conf.urls import url
from .views import LoginView, RegisterView, IndexView, ProfileView, logoutView

app_name = 'users'
# machea en orden la lista y para el primero
urlpatterns = [
  url(r'^index/', IndexView.as_view(), name='index'),
  url(r'^login', LoginView.as_view(), name='login'),
  url(r'^logout$', logoutView, name='logout'),
  url(r'^register', RegisterView.as_view(), name='register'),
  url(r'^profile/(?P<pk>[0-9]+)/$', ProfileView.as_view(), name='profile'),
]