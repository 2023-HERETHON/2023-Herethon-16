from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.http import HttpResponseForbidden
from django.utils import timezone

def mypage(request) :
    return render(request, 'mypage.html')

def Post_list(request):
    postlist = Post.objects.all()

    return render(request, 'mytrip.html', {'postlist' : postlist})

def Post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    
    if not post.is_public and not request.user.is_authenticated:
        return HttpResponseForbidden()
    return render(request, 'mytrip_post.html', {'post': post})

def detail(request):
    return render(request, 'mytrip_detail.html')

def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            if 'is_public' not in request.POST:
                post.is_public = False
            post.save()
            return redirect('posts:postlist')
    else:
        form = PostForm(initial={'is_public': True})
    context = {'form':form}
    return render(request, 'mytrip_detail.html', context)