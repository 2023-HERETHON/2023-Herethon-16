from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.conf import settings

#User = get_user_model()

class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, name, **extra_fields):
        if not email :
            raise ValueError('The given email mist be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email = email, username = username, name=name, **extra_fields)
        user.set_password(password)
        user.save (using = self._db)
        return user

    def create_user(self, username = '', password = None, email='', **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, email, **extra_fields)
    
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(username, password, **extra_fields)

class User(AbstractUser) :
    username = models.CharField(verbose_name="id", max_length=30, unique=True)
    email = models.EmailField(verbose_name="email", max_length=255)
    name = models.CharField(verbose_name="사용자명", max_length=10)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []  # 필수로 받고 싶은 필드들 넣기 원래 소스 코드엔 email필드가 들어가지만 우리는 로그인을 이메일로 하니깐..

    def __str__(self):
        return "<%d %s>" % (self.pk, self.email)

class Post(models.Model) :
    title = models.CharField(verbose_name='제목', max_length=50)
    # 여행지 필드..
    duration = models.DurationField(verbose_name='여행기간', null=True)
    # 여행 동행자 
    plan = models.TextField(verbose_name='상세일정', null=True)
    
    # 지도에 표시할 위도 , 경도 
    latitude = models.CharField(verbose_name='위도', max_length=50, null=True)
    longitude = models.CharField(verbose_name='경도', max_length=50, null=True)
    
    record = models.TextField(verbose_name='여행기록', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    like_count = models.IntegerField(verbose_name='좋아요개수', null=True)
    # photo = models.ImageField(verbose_name='이미지', blank=True, null=True, upload_to='post_photo')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', null=True)
    def __str__(self): 
        return self.title

# 댓글에 해당하는 model 정의 
class Comment(models.Model) : 
    comment = models.TextField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True) # 날짜 순으로 댓글 뿌려주기 위해 
    # post 객체를 참조해서 만들 컬럼 -> target_post 
    article = models.ForeignKey(Post, on_delete=models.CASCADE) # 게시글 모델 참조 필드 
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # 게시글 작성자 

    def __str__(self): 
        return self.comment