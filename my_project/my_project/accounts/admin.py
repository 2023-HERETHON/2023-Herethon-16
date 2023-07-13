from django.contrib import admin
from accounts.models import Post, Comment, User

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)