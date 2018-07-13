from django.contrib import admin
from django.urls import include, re_path
from django.urls import path
from shufic import views
from shufic.views import showvideo, onevideo, addlikes, addcomment, hello

urlpatterns = [

    re_path(r'^$', showvideo),
    re_path(r'^addlikes/(?P<video_id>\d+)/$', addlikes),
    re_path(r'^Vaddlikes/(?P<video_id>\d+)/$', addlikes),
    re_path(r'get/(?P<video_id>\d+)/$', onevideo),    #это все что я исправил
    re_path(r'^addcomment/(?P<video_id>\d+)/$', addcomment)
]