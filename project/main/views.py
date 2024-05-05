from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.files.storage import default_storage

from .models import Post

# Create your views here.

def mainpage(request):
    context = {
        'first_to_third' : ['MTV란? - Model , View , Template 를 의미', 'Templates 폴더 - 유저에게 제공할 파일의 구조나 레이아웃을 한 데 모아 관리하는 역할', 'Views.py 파일 - views.py 파일에 함수를 작성함으로써 mainpage 가 렌더링 될 수 있도록 함'],
        'third_step' : ["url 에 해당하는 데이터를 요청(request)" , "데이터에 맞는 html을 전송(render)"],
        'last' : 'urls.py 파일 - main 앱에서 views 파일을 import',
    }
    return render(request , 'main/mainpage.html' , context)

def secondpage(request):
    posts = Post.objects.all()
    return render(request , 'main/secondpage.html', {'posts' : posts})

def new_post(request):
    return render(request, 'main/new-post.html')

def detail(request, id):
    post = get_object_or_404(Post , pk=id)
    return render(request, 'main/detail.html', {'post' : post})

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'post' : edit_post})

#데이터베이스에 저장하는 함수
def create(request):
    new_post = Post()

    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.body = request.POST['body']
    new_post.pub_date = timezone.now()
    new_post.image = request.FILES.get('image')
    new_post.feel = request.POST['feel']
    #post 의 post_user_id 값을 유저의 id 값으로 설정
    new_post.post_user_id = request.user.id
    new_post.save()

    return redirect('main:detail', new_post.id)

def update(request, id):
    update_post = Post.objects.get(pk=id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.body = request.POST['body']
    update_post.pub_date = timezone.now()
    update_post.image = request.FILES.get('image') 
    update_post.feel = request.POST['feel']

    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    default_storage.delete(delete_post.image.path)
    return redirect('main:secondpage')