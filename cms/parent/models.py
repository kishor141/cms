from django.db import models
from django.contrib.auth.models import User
from student.models import Student
from datetime import datetime   
# Create your models here.
class Parent(models.Model):
	user = models.OneToOneField(User, related_name = "parent_user")
	createdOn = models.DateTimeField(auto_now= True)
	age = models.IntegerField(default = 18)
	#dob = models.DateTimeField()
	occupation = models.CharField(max_length = 120)
	parentof = models.ForeignKey(Student, related_name = "parentof_student")
	housename = models.CharField(max_length = 120)
	place = models.CharField(max_length = 120)
	district = models.CharField(max_length = 120)
	state = models.CharField(max_length = 120)
	nationality = models.CharField(max_length = 120)
	contact = models.IntegerField(default = 0)
	altcontact = models.IntegerField(default = 0)

	def __str__(self):
		return self.user.first_name
	

