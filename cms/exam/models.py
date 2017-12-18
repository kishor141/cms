from django.db import models
from course.models import Course, Subject
# Create your models here.

class ExamType(models.Model):
	examtypename = models.CharField(max_length = 120)
	desc = models.CharField(max_length = 220)
	def __str__(self):
		return self.examtypename

class Exam(models.Model):
	course = models.ForeignKey(Course, related_name = 'courseid_exam')
	semester = models.IntegerField(default = 1)
	examname = models.CharField(max_length = 220, default = None)
	examtypename = models.ForeignKey(ExamType, related_name = "examtype_examtype")
	examdesc = models.CharField(max_length = 220, default = None)
	startdate = models.DateTimeField()
	enddate = models.DateTimeField()

	def __str__(self):
		return self.examname

class ExamDetails(models.Model):
	exam = models.ForeignKey(Exam, related_name = 'examid_examdetails')
	examdate = models.DateTimeField()
	subjectid = models.ForeignKey(Subject, related_name = 'subjectid_examdetails')
	desc = models.CharField(max_length = 120)

	def __str__(self):
		return self.examid