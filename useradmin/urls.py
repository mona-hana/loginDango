from django.urls import  path
from useradmin import views

urlpatterns = [
  path('login_admin', views.login_admin ,name='login_admin'),
  path('home' , views.home , name='home'),
  path('home_admin' , views.home_admin , name='home_admin'),
  path('logout_admin', views.logout_admin ,name='logout_admin'),
]
