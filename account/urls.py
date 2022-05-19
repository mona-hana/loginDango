from django.urls import  path
from account import views

urlpatterns = [
  path('newLogin' , views.newLogin , name ='newLogin'),
  path('' , views.index , name='index'),
  path('user_list'  , views.user_list , name='user_list'),
  path('signup_user' , views.signup_user , name='signup_user'),
  path('loginindex' , views.loginindex , name='loginindex'),
  path('logout_user' , views.logout_user , name='logout_user'),
  path('profile' , views.profile , name='profile'),
]
