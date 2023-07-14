from django import forms
#from .models import Post, Comment
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

# 여기서부터 

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','name','phone_number')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username','email','name','phone_number')

    def clean_password(self):
        return self.initial["password"]
# 여기까지 custom User 입력 폼 


# post입력 폼 커스텀 
# class PostBaseForm(forms.Form):
#     title = forms.CharField(label='제목')
#     duration = forms.DurationField(label='여행기간')
    #photo = forms.ImageField('이미지')
    #content = forms.CharField(label='내용', widget=forms.Textarea)


# class PostModelForm(forms.ModelForm) :
#     class Meta:
#             model = Post
#             fields = ['title', 'duration', 'content' ]

# class CommentModelForm(forms.ModelForm) :
#     class Meta:
#             model = Comment
#             fields = ['comment']