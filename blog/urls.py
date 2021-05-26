from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.post_list, name='blog_url_name'),
    path('', views.index, name='index_url_name'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
]
