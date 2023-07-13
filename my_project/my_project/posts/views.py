from django.shortcuts import render
from .models import Post
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
    postlist = Post.objects.all()
    if request.method == 'POST':
        b = Post(
            title = request.POST['title'],
            destination = request.POST['destination'],
            startPeriod = request.POST['startPeriod'],
            endPeriod = request.POST['endPeriod'],
            content = request.POST['content'],
            record = request.POST['record'],
            created_at = timezone.now()
        )
        b.save()
    return HttpResponseRedirect('mytrip.html')