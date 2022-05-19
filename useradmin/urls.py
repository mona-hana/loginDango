from django.urls import  path
from useradmin import views

urlpatterns = [
  path('login_user', views.login_user ,name='login_user'),
  path('home' , views.home , name='home'),
]
