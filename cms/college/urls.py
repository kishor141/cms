from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from . import views
from views import *

urlpatterns = [
	url(r'^$', HomePageView.as_view(), name="home"),
 	url(r'^home', AdminPanelView.as_view(), name = "home"),
 	url(r'^login/',auth_views.login, {'template_name':'login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name = 'logout'),
	# url(r'^profile/(?P<pk>[\w-]+)/$', ProfileView.as_view() , name = "profile"),
]
