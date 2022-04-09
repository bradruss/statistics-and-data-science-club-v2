from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from photos.models import PhotoPost
from .models import Post
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# Create your views here.
def index(request):
    # Import Post models/objects into index.html
    time = timezone.now()
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/index.html', {'posts': posts, 'time': time})

# Want this seperate since we are using different posts for photos
def photo_index(request):
    time = timezone.now()
    posts = PhotoPost.objects.order_by('-created_date')
    return render(request, 'photos/base.html', {'posts': posts, 'time': time})

def people(request):
    return render(request, 'main/people.html')

def software(request):
    return render(request, 'main/software.html')

def links(request):
    return render(request, 'main/links.html')

def asa(request):
    return render(request, 'main/asa.html')

def career_resources(request):
    return render(request, 'main/career_resources.html')

def contact(request):
    return render(request, "main/contact.html")

def success(request):
    return render(request, 'main/success.html')

def photos(request):
    return render(request, 'photos/templates/photos/post_detail.html')

def handler404(request, *args, **kwargs):
    return render(request, 'main/404.html', status=404)

def handler500(request):
    return render(request, 'main/500.html', status=500)

#def post_list(request):

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})