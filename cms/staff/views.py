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

class SuccessView(TemplateView):
	template_name = "staff/success.html"

class RegisterView(FormView):
	template_name = 'staff/registration.html'
	form_class = RegisterForm
	model = User
	

	def get(self, request, *args, **kwargs):
		print("inside get--")
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		profile_form = StaffForm()
		return self.render_to_response(self.get_context_data(form = form, profile_form=profile_form))

	def get_success_url(self,**kwargs):
		print("work reverse lazy")
		return reverse_lazy('staff_success')

	def post(self,request, *args, **kwargs):
		print("-------------inside post------------")
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		profile_form = StaffForm(self.request.POST)
		if (form.is_valid() and profile_form.is_valid()):
			print("form valid returned-------------")
			return self.form_valid(form, profile_form)
		else:
			print("------------form invalid returned............")
			return self.form_invalid(form,profile_form)

	def form_valid(self,form, profile_form):
		self.object = form.save()
		p_form = profile_form.save(commit = False)
		p_form.user = self.object
		p_form.save()
		return super(RegisterView,self).form_valid(form)

	def form_invalid(self, form, profile_form):
		return self.render_to_response(self.get_context_data(form = form,profile_form = profile_form))


class ListAllStaffView(View):
	template_name = "staff/stafflist.html"

	def get(self, request):
		print("inside get")
		stafflist = Staff.objects.all()
		return render_to_response(self.template_name, {'stlist':stafflist})

def updatestaff(request, uid, sid):
	template_name='staff/update_staff.html'
	staff = get_object_or_404(Staff, id= sid) 
	staff_user = get_object_or_404(User, id = uid)   
	print("staff name--", staff.user.first_name)
	print("staff age-- ",staff.age)
	form = RegisterForm(request.POST or None, instance=staff_user)
	profile_form = StaffForm(request.POST or None, instance=staff)
	if form.is_valid():
		form.save()
		profile_form.save()
		return redirect('staff:list_staff')
	return render(request, template_name, {'form':form, 'profile_form':profile_form})

# ---------------------------------------------------------
def deletestaff(request,uid,sid):
	template_name='staff/staff_confirm_delete.html'
	staff = get_object_or_404(Staff, id= sid) 
	staff_user = get_object_or_404(User, id = uid)   
	print("staff name--", staff.user.first_name)
	print("staff age-- ",staff.age)
	if request.method=='POST':
		staff.delete()
		staff_user.delete()
		return redirect('staff:list_staff')
	return render(request, template_name, {'form':staff})
