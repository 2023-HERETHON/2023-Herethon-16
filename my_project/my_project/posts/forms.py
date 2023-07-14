from django import forms
from .models import Post, UserInfo

class PostForm(forms.ModelForm):
    is_public = forms.BooleanField(
        label='게시글을 공개하시겠습니까?',
        required=False,
        widget=forms.CheckboxInput
    )
    class Meta:
        model = Post
        fields = ['title', 'destination', 'startPeriod', 'endPeriod', 'content', 'record', 'is_public', 'latitude', 'longitude']
        widgets = {
            'is_public' : forms.RadioSelect,
        }

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        # fields = '__all__'
        fields = ['profile', 'info', 'travel_place'] 