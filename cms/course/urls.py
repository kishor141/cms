from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
from views import *
urlpatterns = [

url(r'^$', portal_main_page, name="portal_main_page"),url(r'^new/$', RegisterView.as_view(), name = 'new_course'),
url(r'^list/$', ListAllCourseView.as_view(), name='list_course'),
url(r'^update/(?P<pk>[\w-]+)/$', views.updatecourse ,name='course_update'),
url(r'^delete/(?P<pk>[\w-]+)/$', views.deletecourse ,name='course_delete'),
url(r'^detail/(?P<cid>[\w-]+)/$', views.coursedetail ,name='course_detail'),
url(r'^success/', SuccessView.as_view(), name = "course_success"),

url(r'^subject/new/$', RegisterSubjectView.as_view(), name = 'new_subject'),
url(r'^subject/list/$', ListAllSubjectView.as_view(), name='list_subject'),
url(r'^subject/update/(?P<pk>[\w-]+)/$', views.updatesubject, name='subject_update'),
url(r'^subject/delete/(?P<pk>[\w-]+)/$', views.deletesubject, name='subject_delete'),
url(r'^subject/success/', SuccessView.as_view(), name = "subject_success"),

]

