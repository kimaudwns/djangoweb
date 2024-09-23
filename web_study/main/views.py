from urllib import request
from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blog(request):
    # 모든 데이터 변수에 저장 : models의 클래스이름.objects.all()
    posts = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist':posts})
def posting(request,pk):
    # 모든 데이터 변수에 저장 : models의 클래스이름.objects.all()
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
    # 모든 데이터 변수에 저장 : models의 클래스이름.objects.all()
    if request.method == 'POST' :
        if request.POST['mainphoto']:
            new_article = Post.objects.create(
                postname = request.POST['postname'],
                contents = request.POST['contents'],
                mainphoto = request.POST['mainphoto'],
            )
        else:
            new_article = Post.objects.create(
                postname = request.POST['postname'],
                contents = request.POST['contents'],
            )
        return redirect('/blog')
    return render(request,'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html',{'Post':post})

