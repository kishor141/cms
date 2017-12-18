from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length = 120)
	fees = models.IntegerField()
	eligibility = models.CharField(max_length = 120)
	duration = models.IntegerField(default = 3)
	noofsemesters = models.IntegerField(default = 6)
	desc = models.CharField(max_length = 220)
	totseats = models.IntegerField(default = 0)
	balseats = models.IntegerField(default = 0)
	
	def __str__(self):
		return self.name


class Subject(models.Model):
	name = models.CharField(max_length = 120)
	code = models.CharField(max_length = 160)
	desc = models.CharField(max_length = 120)
	course = models.ForeignKey(Course, related_name = "course_name")
	semester = models.CharField(max_length = 120)
	
	def __str__(self):
		return self.name

