from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^propose/$', views.propose, name='ask'),
    url(r'^what_has_been_proposed/$', views.what_has_been_proposed, name='create'),
    url(r'^acceptation/$', views.acceptation, name='answer'),
    url(r'^accepted/$', views.accepted, name='answer'),

]
