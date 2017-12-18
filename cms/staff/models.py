from django.db import models
from django.contrib.auth.models import User
from datetime import datetime   
# Create your models here.
class Staff(models.Model):
	user = models.OneToOneField(User, related_name = "staff_user")
	createdOn = models.DateTimeField(auto_now= True)
	age = models.IntegerField(default = 15)
	#dob = models.DateTimeField()
	designation = models.CharField(max_length = 120)
	housename = models.CharField(max_length = 120)
	place = models.CharField(max_length = 120)
	district = models.CharField(max_length = 120)
	state = models.CharField(max_length = 120)
	nationality = models.CharField(max_length = 120)
	contact = models.IntegerField(default = 0)
	altcontact = models.IntegerField(default = 0)

	def __str__(self):
		return self.user.first_name
	

