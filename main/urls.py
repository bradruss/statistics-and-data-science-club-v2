from django.conf.urls import url
from django.urls import path
from . import views

# https://stackoverflow.com/questions/340888/navigation-in-django

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index_url_name'),
    url(r'^links/$', views.links, name='links_url_name'),
    url(r'^people/$', views.people, name='people_url_name'),
    url(r'^software/$', views.software, name='software_url_name'),
    url(r'^asa/$', views.asa, name='asa_url_name'),
    url(r'^career_resources/$', views.career_resources, name='career_resources_url_name'),
    url(r'^contact/$', views.contact, name='contact_url_name'),
    url(r'^success/$', views.success, name='success_url_name'),
    # url(r'^photos/$', views.photo_index, name='photos_url_name'),
    #path('', views.post_list, name='blog_url_name'),
    path('post/<int:pk>', views.post_detail, name='post_detail')


    # url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), # here
    # url(r'^event/new/$', views.event, name='event_new'),
    # url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]

