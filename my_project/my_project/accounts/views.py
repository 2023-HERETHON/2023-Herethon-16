from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# from .forms import PostBaseForm
# Create your views here.

def signup(request) :
    if request.method == 'POST' :
        id = request.POST['id']
        pw = request.POST['passwd']
        # 회원가입 조건에 따라 if문 조건 수정하기 
        if id is not None and pw is not None :
            new_user = User.objects.create_user(username=id, password=pw)
            auth.login(request, new_user)
            return render(request, 'main.html')

    return render(request, 'signup.html')

def login(request) :
    if request.method == 'POST' :
        id = request.POST['id']
        pw = request.POST['passwd']
        user = auth.authenticate(request, username=id, password=pw)
        if user is not None :
            auth.login(request, user)
            return render(request, 'main.html')
    return render(request, 'login.html')

def logout(request) :
    auth.logout(request)
    return render(request, 'login.html')

def mypage(request) :
    return render(request, 'mypage.html')

def find_id(request) :
    return render(request, 'login.html')

def find_id(request) :
    return render(request, 'login.html')

# 필요하면 post views 파일에 가져다 쓰기 
# def post_create_form(request) :
#     if request.method == 'POST' :
#         form = PostBaseForm(request.POST)

#         return redirect('index.html')
    
#     else : # GET 일때 
#         form = PostBaseForm()
#         return render(request, 'index.html', {'form' : form})
# urls.py에 추가하기 
# pah('post_create/', view.post_create_form, name='post_create')