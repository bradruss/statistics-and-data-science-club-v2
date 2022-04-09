from django.contrib import admin
from .models import PhotoPost
from django_summernote.admin  import SummernoteModelAdmin

# Commented out to solely post photos
# https://summernote.org/examples/#themes-with-bootswatch
# class PhotoPostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)

admin.site.register(PhotoPost)
