from django import forms
from .models import Post, Comment

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

class CommentModelForm(forms.ModelForm) :
    class Meta:
            model = Comment
            fields = ['comment']