from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.Post_list),
    path('<int:pk>/', views.Post_detail),
    path('detail/', views.detail, name='detail'),
    path('detail/write', views.write, name='write'),
    path('mypage/', views.mypage, name='mypage'),
]
