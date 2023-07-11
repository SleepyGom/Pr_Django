from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
# from rest_framework import viewsets
# from .serializers import TaskSerializer
from .models import Post # Task
from .forms import PostForm

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html',{'post_list' : post_list})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
        
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})


def post_update(request,pk):
    post = get_object_or_404(Post,pk)
    if request.method == 'POST':
            form = PostForm(request.POST, intance=post)
            if form.is_vaild():
                post = form.save()
                return redirect('blog:detail', pk=post.pk)
    else:
        form = PostForm(intance = post)
    return render(request, 'blog/post_form.html', {'form':form})

def post_delete(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:list')
    return render(request,'blog/post_confirm_delete.html', {'post':post})


### login
def login_view(request):
    if request.method == 'Post':
        username = request.Post.get('username')
        password = request.Post.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '로그인 완료')
            return redirect('login')
        else:
            messages.error(request, '아이디나 비밀번호를 확인해 주세요')
    return render(request, 'blog/login.html')


def home(request):
    context = {'name' : 'John'}
    return render(request, 'home.html', context)

