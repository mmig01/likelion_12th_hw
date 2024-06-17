from django.shortcuts import get_object_or_404, redirect, render
from main.models import Post, User

# Create your views here.
def mypage(request, id):
    posts = Post.objects.all()
    user = get_object_or_404(User, pk=id)
    followers = user.profile.followers.all()
    followings = user.profile.followings.all()
    context = {
        'target_user':user,
        'posts': posts,
        'followers': followers,
        'followings': followings,
    }
    return render(request , 'users/mypage.html', context)

def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower=user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect("users:mypage", followed_user.id)