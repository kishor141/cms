from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from views import *
from . import views
urlpatterns = [

url(r'^$', portal_main_page, name="portal_main_page"),
url(r'^new/$', RegisterView.as_view(), name = 'new_exam'),
url(r'^list/$', ListAllExamView.as_view(), name='list_exam'),
url(r'^update/(?P<pk>[\w-]+)/$', views.updateexam, name='update_exam'),
url(r'^delete/(?P<pk>[\w-]+)/$', views.deleteexam, name='delete_exam'),
url(r'^success/', SuccessView.as_view(), name = "exam_success"),

]

