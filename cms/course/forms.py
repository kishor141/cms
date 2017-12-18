from django import forms
from captcha.fields import CaptchaField

from models import Course, Subject


class RegisterCourseForm(forms.ModelForm):
	captcha = CaptchaField()

	class Meta:
		model = Course
		fields = ['name','fees','eligibility','duration','noofsemesters','totseats','balseats','desc']

	def __init__(self,*args,**kwargs):
		super(RegisterCourseForm, self).__init__(*args, **kwargs)


class RegisterSubjectForm(forms.ModelForm):
	captcha = CaptchaField()

	class Meta:
		model = Subject
		fields = ['name','code','desc','course','semester']

	def __init__(self,*args,**kwargs):
		super(RegisterSubjectForm, self).__init__(*args, **kwargs)

