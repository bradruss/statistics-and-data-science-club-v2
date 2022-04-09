from django.shortcuts import render
from django.utils import timezone
from .models import PhotoPost
from django.shortcuts import render, get_object_or_404
from django.db.models import Max

# This section is copy/pasted from blog, but we change it to post_list instead of index

def photo_index(request):

    # Get time
    time = timezone.now()

    # Get indeces for ids
    values = PhotoPost.objects.all().values()

    # Find max of values
    max = PhotoPost.objects.aggregate(Max('id'))
    max = max.get('id__max')

    # Fill filter list with certain values from descending from the max id
    # RESULT: filter_list = [max,max - 1,max - 2,max - 3,max-4,max-5,...]
    filter_list = []


    try:
        for x in range(3):
            filter_list.append(max)
            max -= 1
    except TypeError:
        pass

    # With all summernote blog posts ordered by the date created, filter in latest X posts
    posts = PhotoPost.objects.order_by('-created_date').filter(id__in=filter_list) # .filter(id__lte=6)
    return render(request, 'photos/post_list.html', {'posts': posts, 'time': time, 'values': values, 'max' : max, 'filter_list': filter_list})


def post_list(request):
    time = timezone.now()
    posts = PhotoPost.objects.order_by('-created_date')
    return render(request, 'photos/post_list.html', {'posts': posts, 'time': time, 'range': range(6)})


def post_detail(request, pk):
    post = get_object_or_404(PhotoPost, pk=pk)
    return render(request, 'photos/post_detail.html', {'post': post})
