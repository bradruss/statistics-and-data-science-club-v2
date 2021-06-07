from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.db.models import Max


def index(request):

    # Get time
    time = timezone.now()

    # Get indeces for ids
    values = Post.objects.all().values()

    # Find max of values
    max = Post.objects.aggregate(Max('id'))
    max = max.get('id__max')

    # Fill filter list with certain values from descending from the max id
    # RESULT: filter_list = [max,max - 1,max - 2,max - 3,max-4,max-5,...]
    filter_list = []
    for x in range(3):
        filter_list.append(max)
        max -= 1

    # With all summernote blog posts ordered by the date created, filter in latest X posts
    posts = Post.objects.order_by('-created_date').filter(id__in=filter_list) # .filter(id__lte=6)
    return render(request, 'blog/index.html', {'posts': posts, 'time': time, 'values': values, 'max' : max, 'filter_list': filter_list})


def post_list(request):
    time = timezone.now()
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'time': time, 'range': range(6)})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
