from django.shortcuts import render
from .models import Post # 동일 폴더의 models에서 Post를 가져옴 

def home(request):
    posts = Post.objects
    return render(request, "post/index.html", {'posts': posts})