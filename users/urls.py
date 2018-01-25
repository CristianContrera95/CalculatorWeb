from django.conf.urls import url
from .views import LoginView, RegisterView, IndexView,logoutView

app_name = 'users'
# machea en orden la lista y para el primero
urlpatterns = [
  url(r'^index/', IndexView.as_view(), name='index'),
  url(r'^login', LoginView.as_view(), name='login'),
  url(r'^logout$', logoutView, name='logout'),
  url(r'^register', RegisterView.as_view(), name='register'),
  #url(r'^auth', auth, name='auth'),
  #url(r'^profile/(?P<user_id>[0-9]+)/$', profile, name='profile'),

]