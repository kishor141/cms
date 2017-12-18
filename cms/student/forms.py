from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from django import forms
from captcha.fields import CaptchaField

from student.models import *

# class CaptchaForm(forms.ModelForm):
	
# 	class Meta:
# 		model = Student


class RegisterForm(UserCreationForm):
	first_name = forms.CharField(required = True,label = 'First Name',max_length = 32)
	last_name = forms.CharField(required = True,label = 'Last Name',max_length = 32)
	email = forms.EmailField(required = True,label = 'Email',max_length = 32,)
	username = forms.CharField(required = True,label = 'Username',max_length = 32)

	class Meta:
		model = User
		fields = ('first_name','last_name','email','username','password1','password2')

	def __init__(self,*args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2:
			if password1 != password2:
				print("invalid password")
				raise forms.ValidationError("Password mismatch")
			return password2

	def clean_email(self):
		
		if self.cleaned_data.get('email')== '':
			print("invalid email")
			raise forms.ValidationError("invalid email")
		else:
			return self.cleaned_data.get('email')
	
	
	

class StudentForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Student
		exclude = ('user',)

	def __init__(self,*args,**kwargs):
		super(StudentForm, self).__init__(*args, **kwargs)

