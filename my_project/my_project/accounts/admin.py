from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm,UserChangeForm
from .models import *
from posts.models import *

#from .models import User

# Register your models here.
#admin.site.register(User)

# 여기서 부터 
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username','email','name','phone_number','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None,{'fields':('username','email','password')}),
        ("Personal info",{'fields':('name','phone_number')}),
        ("Permissions",{'fields':('is_admin',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'name','phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def has_change_permission(self, request, obj=None):
        return True
#admin.site.register(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
#여기까지 custom User부분 