from django.contrib import admin
from .models import Blog_Post

from django_summernote.admin  import SummernoteModelAdmin

# Register model for summernote blog posts
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Blog_Post, PostAdmin)