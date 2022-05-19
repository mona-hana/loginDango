from django.urls import path
from blog.views import post_new , post_list , post_detail ,post_edit , post , postList


urlpatterns = [
    path('post/<int:pk>/',post_detail, name='post_detail'),
    path('post/<int:pk>/edit/',post_edit, name='post_edit'),
    path('post_list', post_list, name='post_list'),
    path('post_new', post_new, name='post_new'),
    path('post', post , name='post' ) ,
    #path('postList', postList, name='postList' ) ,
   
   
]