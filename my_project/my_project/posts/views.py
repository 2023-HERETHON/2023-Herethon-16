from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, UserInfo
from .forms import PostForm, UserInfoForm
from django.http import HttpResponseForbidden
from django.utils import timezone

def mypage(request) :
    return render(request, 'mypage.html')

def aboutus(request) :
    return render(request, 'aboutus.html')

def Community(request) :
    return render(request, 'Community.html')

def WomenZone(request) :
    return render(request, 'women_main.html')

def Post_list(request):
    postlist = Post.objects.all().order_by('-pk')

    return render(request, 'mytrip.html', {'postlist' : postlist})

def Post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    # if not post.is_public and not request.user.is_authenticated:
    #     return HttpResponseForbidden()
    return render(request, 'mytrip_post.html', {'post': post})

def detail(request):
    return render(request, 'mytrip_detail.html')

def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            is_public = request.POST.get('is_public', 'True') == 'True'
            post.is_public = is_public
            post.latitude = request.POST.get('latitude', None)  # 위도 값 가져오기
            post.longitude = request.POST.get('longitude', None)
            post.save()
            print(post.created_at)
            return redirect('posts:postlist')
    else:
        form = PostForm(initial={'is_public': True})
        print("실패!!")
    context = {'form': form}
    return render(request, 'mytrip_detail.html', context)

def mypage_info(request) :
    user_info = get_object_or_404(UserInfo, pk=request.user.id)
    if request.method == 'POST' or request.method == 'FILES' :
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.user = request.user
            form.profile = request.FILES
            form.info = request.POST['info']
            form.travel_place = request.POST['travel_place']
            form.save()
            print('저장')
            return redirect('mypage')
    else:
        print('GET')
        # form = UserInfoForm(instance=user_info)
        forms = UserInfoForm(instance=user_info)
    return render(request, 'me.html',{'forms':forms})