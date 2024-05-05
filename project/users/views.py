from django.shortcuts import render
from main.models import Post

# Create your views here.
def mypage(request):
    posts = Post.objects.all()
    return render(request , 'users/mypage.html', {'posts' : posts})