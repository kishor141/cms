from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from views import *
from . import views

urlpatterns = [

url(r'^$', portal_main_page, name="portal_main_page"),url(r'^new/$', RegisterView.as_view(), name = 'new_staff'),
url(r'^list/$', ListAllStaffView.as_view(), name='list_staff'),
url(r'^update/(?P<uid>[\w-]+)/(?P<sid>[\w-]+)/$', views.updatestaff, name='update_staff'),
url(r'^delete/(?P<uid>[\w-]+)/(?P<sid>[\w-]+)/$', views.deletestaff, name='delete_staff'),
url(r'^success/', SuccessView.as_view(), name = "staff_success"),

]

