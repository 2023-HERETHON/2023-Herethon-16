from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('findaccount/', views.findaccount, name='findaccount'),
    path('mypage', views.mypage, name='mypage')
]