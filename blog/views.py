from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


def index(request):
    time = timezone.now()
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/index.html', {'posts': posts, 'time': time})


def post_list(request):
    time = timezone.now()
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'time': time})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
