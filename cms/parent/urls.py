from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from views import *
from . import views

urlpatterns = [

url(r'^$', portal_main_page, name="portal_main_page"),url(r'^new/$', RegisterView.as_view(), name = 'new_parent'),
url(r'^list/$', ListAllParentView.as_view(), name='list_parent'),
url(r'^update/(?P<uid>[\w-]+)/(?P<pid>[\w-]+)/$', views.updateparent, name='update_parent'),
url(r'^delete/(?P<uid>[\w-]+)/(?P<pid>[\w-]+)/$', views.deleteparent, name='delete_parent'),
url(r'^success/', SuccessView.as_view(), name = "parent_success"),
]