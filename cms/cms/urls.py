"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    url(r'',include('college.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^college/', include('college.urls', namespace = "college")),
    url(r'^student/', include('student.urls', namespace = "student")),
    url(r'^parent/', include('parent.urls', namespace = "parent")),
    url(r'^staff/', include('staff.urls', namespace = "staff")),
    url(r'^exam/', include('exam.urls', namespace = "exam")),
    url(r'^course/', include('course.urls', namespace = "course")),
    
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    ]



urlpatterns += [
    url(r'^captcha/', include('captcha.urls')),
]