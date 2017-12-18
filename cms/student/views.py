from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.core.urlresolvers import reverse
from forms import *

@login_required
def portal_main_page(request):
	template_name = "index.html"
	return render_to_response('admin_panel.html')

class SuccessView(TemplateView):
	template_name = "success.html"

class RegisterView(FormView):
	template_name = 'student/registration.html'
	form_class = RegisterForm
	model = User
	

	def get(self, request, *args, **kwargs):
		print("inside get--")
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		profile_form = StudentForm()
		return self.render_to_response(self.get_context_data(form = form, profile_form=profile_form))

	def get_success_url(self,**kwargs):
		print("work reverse lazy")
		return reverse_lazy('student:list_student')


	def post(self,request, *args, **kwargs):
		print("-------------inside post------------")
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		profile_form = StudentForm(self.request.POST)
		if (form.is_valid() and profile_form.is_valid()):
			human = True
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


class ListAllStudentView(View):
	template_name = "student/studentlist.html"

	def get(self, request):
		print("inside get")
		studentlist = Student.objects.all()
		return render_to_response(self.template_name, {'stdlist':studentlist})

# def updatestudent(request, uid, sid):
# 	template_name='student/update_student.html'
# 	student = get_object_or_404(Student, id= sid) 
# 	student_user = get_object_or_404(User, id = uid)   
# 	print("student name--", student.user.first_name)
# 	print("student age-- ",student.age)
# 	form = RegisterForm(request.POST or None, instance=student_user)
# 	profile_form = StudentForm(request.POST or None, instance=student)
# 	if form.is_valid():
# 		form.save()
# 		profile_form.save()
# 		return redirect('student:list_student')
# 	return render(request, template_name, {'form':form, 'profile_form':profile_form})

# ---------------------------------------------------------

class UpdateStudent(View):
	template_name = 'student/update_student.html'

	def get(self,request, pk):
		student = Student.objects.get(id = pk)
		form = RegisterForm(instance = student.user)
		profile_form = StudentForm(instance = student)
		return render(request, self.template_name,{'form':form,'profile_form':profile_form})

class DeleteStudent(View):
	template_name='student/student_list.html'
	
	def get(self, request,pk):
		student = Student.objects.get(id= pk) 
		student_user = User.objects.get(id = student.user_id)
		print(student, student_user)   
		print("student name--", student.user.first_name)
		print("student age-- ",student.age)
		student.delete()
		student_user.delete()
		return redirect('student:list_student')

class StudentProfile(View):
	template_name = 'profile.html'
	def get(self,request):
		user_obj = User.objects.get(username = request.user)
		stud_obj = Student.objects.get(user = user_obj)


		context = {
		'name': user_obj.first_name,
		'address':stud_obj.address
		}

		return render_to_response(self.template_name , {'context':context})	