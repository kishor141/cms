from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import FormView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from models import Course, Subject
from exam.forms import *

@login_required
def portal_main_page(request):
	template_name = "index.html"
	return render_to_response('admin_panel.html')
class SuccessView(TemplateView):
	template_name = "success.html"

class RegisterView(FormView):
	template_name = 'exam/registration.html'
	form_class = ExamForm
	model = Exam
	

	def get(self, request, *args, **kwargs):
		print("inside get--")
		exam_form = ExamForm()
		return self.render_to_response(self.get_context_data(exam_form = exam_form))

	def get_success_url(self,**kwargs):
		print("work reverse lazy")
		return reverse_lazy('exam:list_exam')


	def post(self,request, *args, **kwargs):
		print("-------------inside post------------")
		
		exam_form = ExamForm(self.request.POST)
		if (exam_form.is_valid()):
			print("form valid returned-------------")
			return self.form_valid(exam_form)
		else:
			print("------------form invalid returned............")
			return self.form_invalid(exam_form)

	def form_valid(self,exam_form):
		self.object = exam_form.save()
		return super(RegisterView,self).form_valid(exam_form)

	def form_invalid(self, exam_form):
		return self.render_to_response(self.get_context_data(exam_form = exam_form))


class ListAllExamView(View):
	template_name = "exam/examlist.html"

	def get(self, request):
		print("inside get")
		examlist = Exam.objects.all()
		return render_to_response(self.template_name, {'elist':examlist})

def deleteexam(request, pk):
    template_name='exam/exam_confirm_delete.html'
    exam = get_object_or_404(Exam, pk=pk)    
    if request.method=='POST':
        exam.delete()
        return redirect('exam:list_exam')
    return render(request, template_name, {'form':exam})

def updateexam(request, pk):
    template_name='exam/update_exam.html'
    exam = get_object_or_404(Exam, pk=pk)
    form = ExamForm(request.POST or None, instance=exam)
    if form.is_valid():
        form.save()
        return redirect('exam:list_exam')
    return render(request, template_name, {'form':form})

# ---------------------------------------------------------
