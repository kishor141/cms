from django.db import models
from django.contrib.auth.models import User
from datetime import datetime    

# Create your models here.
class Student(models.Model):
	user = models.OneToOneField(User, related_name = "student_user")
	createdOn = models.DateTimeField(auto_now= True)
	age = models.IntegerField(default = 18)
	# dob = models.DateTimeField(blank = True, null = True)
	housename = models.CharField(max_length = 120)
	place = models.CharField(max_length = 120)
	district = models.CharField(max_length = 120)
	state = models.CharField(max_length = 120)
	nationality = models.CharField(max_length = 120)
	contact = models.IntegerField(default = 0)
	altcontact = models.IntegerField(default = 0)
	school10 = models.CharField(max_length = 120)
	marks10 = models.IntegerField(default = 0)
	school12 = models.CharField(max_length = 120)
	marks12 = models.IntegerField(default = 0)


	def __str__(self):
		return self.user.first_name

class attendence(models.Model):
	student = models.ForeignKey(Student, related_name = "student_attendence")
	attended = models.BooleanField(default = False)
	date = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.student.first_name