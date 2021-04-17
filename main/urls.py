from django.conf.urls import url
from . import views
from django.urls import path, include

# https://stackoverflow.com/questions/340888/navigation-in-django

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index_url_name'),
    url(r'^links/$', views.links, name='links_url_name'),
    url(r'^people/$', views.people, name='people_url_name'),
    url(r'^software/$', views.software, name='software_url_name'),
    url(r'^asa/$', views.asa, name='asa_url_name'),

    # New links for career + contact
    url(r'^career_resources/$', views.career_resources, name='career_resources_url_name'),
    path('contact/', include('contactform.urls')),
    url(r'^contact/$', views.contact, name='contact_url_name')


    # url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), # here
    # url(r'^event/new/$', views.event, name='event_new'),
    # url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]

