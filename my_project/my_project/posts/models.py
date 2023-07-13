from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(verbose_name='제목', max_length=20)
    destination = models.CharField(verbose_name='여행지', max_length=20)
    # 여행 시작 ~ 끝 기간
    startPeriod = models.DateField(verbose_name='여행시작')
    endPeriod = models.DateField(verbose_name='여행끝')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    content = models.TextField(verbose_name='상세일정')
    record = models.TextField(verbose_name='여행기록')

    like_count = models.IntegerField(verbose_name='좋아요개수', null=True, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', null=True, blank=True)

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self):
        return f'posts/{self.pk}/'
    