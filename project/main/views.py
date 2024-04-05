from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {
        'first_to_third' : ['MTV란? - Model , View , Template 를 의미', 'Templates 폴더 - 유저에게 제공할 파일의 구조나 레이아웃을 한 데 모아 관리하는 역할', 'Views.py 파일 - views.py 파일에 함수를 작성함으로써 mainpage 가 렌더링 될 수 있도록 함'],
        'third_step' : ["url 에 해당하는 데이터를 요청(request)" , "데이터에 맞는 html을 전송(render)"],
        'last' : 'urls.py 파일 - main 앱에서 views 파일을 import',
    }
    return render(request , 'main/mainpage.html' , context)
def secondpage(request):
    return render(request , 'main/secondpage.html')
