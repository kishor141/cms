from django.db import models
from django.contrib.auth.models import User

from student.models import *
# Create your models here.





# class Events(models.Model):
# 	name = models.CharField(max_length = 120)
# 	desc = models.CharField(max_length = 120)
# 	date = models.DateTimeField()

# class News(models.Model):
# 	title = models.CharField(max_length = 120)
# 	desc = models.CharField(max_length = 120)
# 	date = models.DateTimeField()


# class Marks(models.Model):
# 	student_id = models.OneToOneField(Student, related_name = 'marks_student')
# 	exam_id = models.OneToOneField(Exam, related_name = "marks_exam")
# 	subject_id = models.OneToOneField(Subject, related_name = "marks_subject")
# 	total_mark = models.IntegerField(default = 100)
# 	marks_scored = models.IntegerField(default = 0)

# class FeedbackAnon(models.Model):
# 	message = models.CharField(max_length =220)
# 	date = models.DateTimeField(auto_now = True)


# class FeedbackReg(models.Model):
# 	user_id = models.OneToOneField(User, related_name = "feedbackreg_user")
# 	message = models.CharField(max_length =220)
# 	date = models.DateTimeField(auto_now = True)
# class Notice(models.Model):
# 	issued_by = models.OneToOneField(Staff, related_name = "issued_by_staff")
# 	issued_to = models.CharField(max_length = 120)

	
# 	