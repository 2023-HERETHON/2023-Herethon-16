
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings

User = get_user_model()

# class Post(models.Model) :
#     title = models.CharField(verbose_name='제목', max_length=50)
#     # 여행지 필드..
#     duration = models.DurationField(verbose_name='여행기간', null=True)
#     # 여행 동행자 
#     plan = models.TextField(verbose_name='상세일정')
#     # 지도 어떻게 저장할지 
#     record = models.TextField(verbose_name='여행기록')
#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     create_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
#     like_count = models.IntegerField(verbose_name='좋아요개수', null=True)
#     # photo = models.ImageField(verbose_name='이미지', blank=True, null=True, upload_to='post_photo')
#     likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes')
#     def __str__(self): 
#         return self.title

# # 댓글에 해당하는 model 정의 
# class Comment(models.Model) : 
#     comment = models.TextField(max_length=200, null=True, blank=True)
#     date = models.DateTimeField(auto_now_add=True) # 날짜 순으로 댓글 뿌려주기 위해 
#     # post 객체를 참조해서 만들 컬럼 -> target_post 
#     article = models.ForeignKey(Post, on_delete=models.CASCADE) # 게시글 모델 참조 필드 
#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # 게시글 작성자 

#     def __str__(self): 
#         return self.comment