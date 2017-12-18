from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from views import *
from . import views

urlpatterns = [

url(r'^$', portal_main_page, name="portal_main_page"),
url(r'^new/$', RegisterView.as_view(), name = 'new_student'),
url(r'^list/$', ListAllStudentView.as_view(), name='list_student'),
url(r'^update/(?P<pk>[\w-]+)/$',UpdateStudent.as_view() ,name='student_update'),
url(r'^delete/(?P<pk>[\w-]+)/$', DeleteStudent.as_view(), name='student_delete'),

url(r'^success/', SuccessView.as_view(), name = "student_success"),
]