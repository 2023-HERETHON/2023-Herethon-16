from django.urls import path
from posts import views 
urlpatterns = [
    path('', views.post_main, name='main'),
    path('mypage/', views.mypage, name='mypage'),

    path('create/', views.post_create, name='post_create'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
    # 좋아요 누른 게시글 리스트
    # path('post_like_list/', views.post_like_list, name='post_like_list'),
    
    # comment 경로 
    # path('create_comment/<int:id>', views.create_comment, name='create_comment'),
    # path('update_comment/<int:post_id>/<int:com_id>', views.update_comment, name='update_comment'),
    # path('delete_comment/<int:post_id>/<int:com_id>', views.delete_comment, name='delete_comment'),  

]
