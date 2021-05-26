from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.db.models import Max


def index(request):
    time = timezone.now()
    # Get indeces for last 4 blog posts
    #len(Post.objects)

    # Get indeces for ids
    values = Post.objects.all().values()

    # Find max of values
    max = Post.objects.aggregate(Max('id'))
    max = max.get('id__max')


    # With all summernote blog posts ordered by the date created, filter in latest 4 posts
    # Post.objects returns a QuerySet
    posts = Post.objects.order_by('-created_date').filter(id__in=[24,25,26,23]) # .filter(id__lte=6)
    return render(request, 'blog/index.html', {'posts': posts, 'time': time, 'values': values, 'max' : max})


def post_list(request):
    time = timezone.now()
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'time': time, 'range': range(6)})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
