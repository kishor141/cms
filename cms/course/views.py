from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import FormView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from django.core.urlresolvers import reverse

from models import Course, Subject
from forms import *

@login_required
def portal_main_page(request):
	template_name = "index.html"
	return render_to_response('admin_panel.html')

class SuccessView(TemplateView):
	template_name = "success.html"



class RegisterView(FormView):
	template_name = 'course/registration.html'
	form_class = RegisterCourseForm
	model = Course
	

	def get(self, request, *args, **kwargs):
		print("inside get--")
		course_form = RegisterCourseForm()
		return self.render_to_response(self.get_context_data(course_form = course_form))

	def get_success_url(self,**kwargs):
		print("work reverse lazy")
		return reverse_lazy('course:list_course')


	def post(self,request, *args, **kwargs):
		print("-------------inside post------------")
		
		course_form = RegisterCourseForm(self.request.POST)
		if (course_form.is_valid()):
			print("form valid returned-------------")
			return self.form_valid(course_form)
		else:
			print("------------form invalid returned............")
			return self.form_invalid(course_form)

	def form_valid(self,course_form):
		self.object = course_form.save()
		return super(RegisterView,self).form_valid(course_form)

	def form_invalid(self, course_form):
		return self.render_to_response(self.get_context_data(course_form = course_form))


class ListAllCourseView(View):
	template_name = "course/courselist.html"

	def get(self, request):
		print("inside get")
		courselist = Course.objects.all()
		return render_to_response(self.template_name, {'clist':courselist})

# ---------------------------------------------------

def updatecourse(request, pk):
    template_name='course/update_course.html'
    course = get_object_or_404(Course, pk=pk)
    form = RegisterCourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('course:list_course')
    return render(request, template_name, {'form':form})

def updatesubject(request, pk):
    template_name='course/update_subject.html'
    subject = get_object_or_404(Subject, pk=pk)
    form = RegisterSubjectForm(request.POST or None, instance=subject)
    if form.is_valid():
        form.save()
        return redirect('course:list_subject')
    return render(request, template_name, {'form':form})

# -----------------------------------------

class RegisterSubjectView(FormView):
	template_name = 'course/new_subject.html'
	form_class = RegisterSubjectForm
	model = Subject
	

	def get(self, request, *args, **kwargs):
		print("inside get--")
		subject_form = RegisterSubjectForm()
		return self.render_to_response(self.get_context_data(subject_form = subject_form))

	def get_success_url(self,**kwargs):
		print("work reverse lazy")
		return reverse_lazy('course:list_subject')


	def post(self,request, *args, **kwargs):
		print("-------------inside post------------")
		
		subject_form = RegisterSubjectForm(self.request.POST)
		if (subject_form.is_valid()):
			print("form valid returned-------------")
			return self.form_valid(subject_form)
		else:
			print("------------form invalid returned............")
			return self.form_invalid(subject_form)

	def form_valid(self,subject_form):
		self.object = subject_form.save()
		return super(RegisterSubjectView,self).form_valid(subject_form)

	def form_invalid(self, subject_form):
		return self.render_to_response(self.get_context_data(subject_form = subject_form))


class ListAllSubjectView(View):
	template_name = "course/subjectlist.html"

	def get(self, request):
		print("inside get")
		subjectlist = Subject.objects.all()
		return render_to_response(self.template_name, {'slist':subjectlist})

# ---------------------------------------------------------


def deletesubject(request, pk):
    template_name='course/subject_confirm_delete.html'
    course = get_object_or_404(Subject, pk=pk)    
    if request.method=='POST':
        course.delete()
        return redirect('course:list_subject')
    return render(request, template_name, {'form':course})

def deletecourse(request, pk):
    template_name='course/course_confirm_delete.html'
    course = get_object_or_404(Course, pk=pk)    
    

    if request.method=='POST':
        course.delete()
       
        return redirect('course:list_course')
    return render(request, template_name, {'form':course})


	
# class DeleteSubject(DeleteView):
# 	model = Subject
# 	form_class = RegisterSubjectForm
# 	template_name = 'course/subject_delete.html'
# 	success_url = reverse_lazy('course:list_subject')


# class DeleteCourse(DeleteView):
# 	model = Course
# 	form_class = RegisterCourseForm
# 	template_name = 'course/delete.html'
# 	success_url = reverse_lazy('course:list_course')

# ---------------------------------------------------------




def coursedetail(request, cid):
	template_name='course/course_detail.html'
	course = get_object_or_404(Course, id= cid)
	subjectlist = Subject.objects.filter(course_id = cid) 
	print(course.name, course.fees)
	print(subjectlist)

	return render_to_response(template_name, {'slist':subjectlist})
