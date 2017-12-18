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
	template_name = "success.html"

class RegisterView(FormView):
	template_name = 'parent/registration.html'
	form_class = RegisterForm
	model = User
	
	def get(self, request, *args, **kwargs):
		print("inside get--")
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		profile_form = ParentForm()
		return self.render_to_response(self.get_context_data(form = form, profile_form=profile_form))

	def get_success_url(self,**kwargs):
		print("work reverse lazy")
		return reverse_lazy('parent:list_parent')


	def post(self,request, *args, **kwargs):
		print("-------------inside post------------")
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		profile_form = ParentForm(self.request.POST)
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


class ListAllParentView(View):
	template_name = "parent/parentlist.html"

	def get(self, request):
		print("inside get")
		parentlist = Parent.objects.all()
		return render_to_response(self.template_name, {'parlist':parentlist})


def updateparent(request, uid, pid):
	template_name='parent/update_parent.html'
	parent = get_object_or_404(Parent, id= pid) 
	parent_user = get_object_or_404(User, id = uid)   
	print("parent name--", parent.user.first_name)
	print("parent age-- ",parent.age)
	form = RegisterForm(request.POST or None, instance=parent_user)
	profile_form = ParentForm(request.POST or None,instance=parent)
	if form.is_valid() and profile_form.is_valid():
		form.save()
		profile_form.save()
		return redirect('parent:list_parent')
	return render(request, template_name, {'form':form, 'profile_form':profile_form})

# ---------------------------------------------------------
def deleteparent(request,uid,pid):
	template_name='parent/parent_confirm_delete.html'
	parent = get_object_or_404(Parent, id= pid) 
	parent_user = get_object_or_404(User, id = uid)   
	print("parent name--", parent.user.first_name)
	print("parent age-- ",parent.age)
	if request.method=='POST':
		parent.delete()
		parent_user.delete()
		return redirect('parent:list_parent')
	return render(request, template_name, {'form':parent})
