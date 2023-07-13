from django.contrib import admin
from django.urls import path, include, re_path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # accounts
    path('', views.login, name='login'),
    path('accounts/', include('accounts.urls')),
    # posts
    path('posts/', include('posts.urls')),


    # 소셜로그인
    path('authaccounts/', include('allauth.urls')),
    # 카카오 소셜 로그인 
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^accounts/', include('allauth.urls')),
]
