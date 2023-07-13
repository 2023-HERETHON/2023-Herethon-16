from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User

User = get_user_model()
# class UserManager(BaseUserManager):
#     def _create_user(self, email, username, password, name, **extra_fields):

#         email = self.normalize_email(email)
#         username = self.model.normalize_username(username)
#         user = self.model(email = email, username = username, name=name, **extra_fields)
#         user.set_password(password)
#         user.save (using = self._db)
#         return user

#     def create_user(self, username = '', password = None, name='', email='', **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(username, password, name, email, **extra_fields)

#     def create_superuser(self, username, password, email, name, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff = True')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser = True')

#         return self._create_user(username, password, email, name, **extra_fields)

# class User(AbstractUser) :
#     username = models.CharField(verbose_name="id", max_length=30, unique=True)
#     email = models.EmailField(verbose_name="email", max_length=255)
#     name = models.CharField(verbose_name="사용자명", max_length=10)
#     objects = UserManager()

#     USERNAME_FIELD = 'username'

#     REQUIRED_FIELDS = ['email', 'name']  # 필수로 받고 싶은 필드

#     def __str__(self):
#         return "<%d %s>" % (self.pk, self.username)

# class auth(object):
#     # 이 클래스를 정의하여 settings 에 auth backend로 등록하면 authenticate함수를 아래 처럼 커스터마이징 하여 사용할 수 있다.
#     def authenticate(self, **kwargs):
#         from django.contrib.auth import get_user_model
#         email_id = kwargs.get('email_id')
#         password = kwargs.get('password')
#         try:
#             user = get_user_model().objects.get(email_id=email_id)
#         except:
#             # 유저가 존재하지 않음
#             return None
#         if user.status == 'LOCKED':
#             # 유저 상태가 잠금인 경우
#             raise Exception('USER IS LOCKED')
            
#         if user.login_fail_count >= 5:
#             # 로그인 실패 횟수가 5회 이상이면 로그인 불가
#             raise Exception('PASSWORD FAILED BY 5 TIMES')
        
#         if str(user.password) == hashlib.sha256(password).hexdigest():
#             # 패스워드 일치 => 로그인 성공
#             user.login_fail_count = 0 # 패스워드 실패 횟수를 0으로 초기화
#             user.save(update_fields=['login_fail_count'])
#             return user
#         else:
#             # 패스워드 불일치 => 로그인 실패
#             user.login_fail_count += 1
#             user.save(update_fields=['login_fail_count'])
#             return None
        
# class Post(models.Model) :
#     title = models.CharField(verbose_name='제목', max_length=50)
#     # 여행지 필드..
#     duration = models.DurationField(verbose_name='여행기간', null=True)
#     # 여행 동행자 
#     plan = models.TextField(verbose_name='상세일정', null=True)
    
#     # 지도에 표시할 위도 , 경도 
#     latitude = models.CharField(verbose_name='위도', max_length=50, null=True)
#     longitude = models.CharField(verbose_name='경도', max_length=50, null=True)
    
#     record = models.TextField(verbose_name='여행기록', null=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     create_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
#     like_count = models.IntegerField(verbose_name='좋아요개수', null=True)
#     # photo = models.ImageField(verbose_name='이미지', blank=True, null=True, upload_to='post_photo')
#     likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', null=True)
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