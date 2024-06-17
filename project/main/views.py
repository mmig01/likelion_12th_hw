from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.files.storage import default_storage

from .models import Post, Comment, Tag

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
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {'post':post, 'comments': comments})
    
    elif request.method == 'POST':
        new_comment = Comment()
        # foreignkey -> blog 와 user 객체 넣어주기
        new_comment.post = post
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()

        new_comment.save()
        return redirect('main:detail', id)
    return render(request, 'main/detail.html', {'post' : post})

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'post' : edit_post})

#데이터베이스에 저장하는 함수
def create(request):
    if request.user.is_authenticated:
        new_post = Post()

        new_post.title = request.POST['title']
        new_post.writer = request.user
        new_post.body = request.POST['body']
        new_post.pub_date = timezone.now()
        new_post.image = request.FILES.get('image')
        new_post.feel = request.POST['feel']
        #post 의 post_user_id 값을 유저의 id 값으로 설정
        new_post.save()

         #본문을 띄어쓰기 기준으로 나누기
        words = new_post.body.split(' ')
        tag_list = []

        for w in words:
            if len(w)>0:
                if w[0] == "#":
                    tag_list.append(w[1:])

        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_post.tags.add(tag.id)

        return redirect('main:detail', new_post.id)
    else:
        return redirect('accounts:login')
    
def update(request, id):
    update_post = Post.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_post.writer:
        update_post.title = request.POST['title']
        update_post.body = request.POST['body']
        update_post.feel = request.POST['feel']
        update_post.pub_date = timezone.now()
        if request.FILES.get('image'):
            update_post.image = request.FILES['image']
        if request.FILES.get('feel'):
            update_post.image = request.FILES['image']

        update_post.save()
        return redirect('main:detail', update_post.id)
    return redirect('accounts:login', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(pk=id)
    if delete_post.image:
        default_storage.delete(delete_post.image.path)
    delete_post.delete()
    return redirect('main:secondpage')

def tag_list(request): # 모든 태그 목록을 볼 수 있는 페이지
    tags = Tag.objects.all()
    return render(request, 'main/tag-list.html', {'tags' : tags})

def tag_posts(request, tag_id): # 특정 태그를 가진 게시글의 목록을 볼 수 있는 페이지
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.all()
    return render(request, 'main/tag-post.html', {
        'tag' : tag,
        'posts' : posts
    })

def delete_comment(request, id):
    delete_comment = Comment.objects.get(pk=id)
    # 현재 게시물의 detail 페이지로 돌아가기 위한 post 객체
    current_post = delete_comment.post 
    delete_comment.delete()
    return redirect('main:detail', current_post.id)

def likes(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()
    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect("main:detail", post.id)