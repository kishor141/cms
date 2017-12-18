from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import FormView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from django.core.urlresolvers import reverse
from forms import *
# Create your views here.


@login_required
def portal_main_page(request):
	template_name = "index.html"

	return render_to_response('admin_panel.html')

class HomePageView(TemplateView):
	template_name = "index.html"

class AdminPanelView(TemplateView):
	template_name = "admin_panel.html"

class StaffPanelView(TemplateView):
	template_name = "staff_panel.html"

class StudentPanelView(TemplateView):
	template_name = "student_panel.html"

