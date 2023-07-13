from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

def Post_list(request):
    postlist = Post.objects.all()
    return render(request, 'mytrip.html', {'postlist' : postlist})

def Post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'mytrip_post.html', {'post': post})

def detail(request):
    return render(request, 'mytrip_detail.html')

def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
        # Post.title = request.POST['title'],
        # destination = request.POST['destination'],
        # startPeriod = request.POST['startPeriod'],
        # endPeriod = request.POST['endPeriod'],
        # content = request.POST['content'],
        # record = request.POST['record'],
            post.created_at = timezone.now()
        #posts = Post(title=title, destination=destination, startPeriod=startPeriod, endPeriod=endPeriod, content=content, record=record, created_at=created_at)
            post.save()
            return redirect('posts:postlist')
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'mytrip_detail.html', context)