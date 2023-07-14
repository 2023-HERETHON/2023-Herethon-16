from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    path('', views.Post_list, name='postlist'),
    path('<int:post_id>/', views.Post_detail, name='postdetail'),
    path('detail/', views.detail, name='detail'),
    path('detail/write', views.write, name='write'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage_info/', views.mypage_info, name='mypage_info'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('community/', views.Community, name='community'),
    path('womenzone/', views.WomenZone, name='womenzone'),
]
