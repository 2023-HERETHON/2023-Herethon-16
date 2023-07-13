from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator # 페이지 구현
from accounts.forms import PostBaseForm
from accounts.models import Post

def post_main(request) :
    return render(request, 'main.html')

def mypage(request) :
    return render(request, 'mypage.html')

def post_create(request) :
    if request.method == 'POST' :
        form = PostBaseForm(request.POST)

        if form.is_valid() :
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            return redirect('post_deatil') # 작성 완료 하면 posthome으로 보내기 
    
    else : # GET 요청 
        form = PostBaseForm()  # form.py 
    return render(request, 'mytrip_detail.html',{'form':form})

def post_detail(request) :
    try:
        post = get_object_or_404(Post, pk=id)
    except Post.DoesNotExist:
        return redirect('main') 
    context = {
        'post' : post,
    }
    return render(request, 'mytrip_post.html', context)
\
