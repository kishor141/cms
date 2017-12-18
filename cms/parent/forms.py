from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField


from parent.models import *


class RegisterForm(UserCreationForm):
	first_name = forms.CharField(required = True)
	last_name = forms.CharField(required = True)
	email = forms.EmailField(required = True)
	username = forms.CharField(required = True)

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
	
	
	

class ParentForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Parent
		exclude = ('user',)

	def __init__(self,*args,**kwargs):
		super(ParentForm, self).__init__(*args, **kwargs)

