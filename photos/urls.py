from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='photos_url_name'),
]
