from django.db import models
from django.conf import settings
from accounts.models import User

class Post(models.Model):
    title = models.CharField(verbose_name='제목', max_length=20)
    destination = models.CharField(verbose_name='여행지', max_length=20)
    # 여행 시작 ~ 끝 기간
    startPeriod = models.DateField(verbose_name='여행시작')
    endPeriod = models.DateField(verbose_name='여행끝')
    head_image = models.ImageField(upload_to='posts/images/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    content = models.TextField(verbose_name='상세일정')
    record = models.TextField(verbose_name='여행기록')
    public_choice = (
        (True, '공개'),
        (False, '비공개'),
    )
    is_public = models.BooleanField(choices=public_choice, default=True)

    latitude = models.FloatField(default=37.566826, null=True, blank=True)
    longitude = models.FloatField(default=126.9786567,null=True, blank=True)

    like_count = models.IntegerField(verbose_name='좋아요개수', null=True, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes',blank=True)

    def __str__(self): 
        return f'[{self.pk}]{self.title}'
    
    def get_absolute_url(self):
        return f'{self.pk}/'
    
class UserInfo(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(verbose_name='프로필사진', blank=True, null=True, upload_to='profile-img')
    #한줄소개
    info = models.CharField(verbose_name='한줄소개', max_length=30, null=True)
    travel_place = models.TextField(verbose_name='여행지역', null=True)
    
    def __str__(self): 
        return self.info