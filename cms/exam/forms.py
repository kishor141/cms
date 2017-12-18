from django import forms
from captcha.fields import CaptchaField

	

from course.models import Course, Subject
from exam.models import *

class ExamForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Exam
		fields = ['course','semester','examname','examtypename','examdesc','startdate','enddate']

	def __init__(self,*args,**kwargs):
		super(ExamForm, self).__init__(*args, **kwargs)

class ExamDetailsForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = ExamDetails
		fields = []