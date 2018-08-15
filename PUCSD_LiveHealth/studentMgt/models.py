# * coding: utf8 *
from __future__ import unicode_literals

from django.db import models

class Student_in_class(models.Model):
	student_class_id = models.IntegerField(primary_key=True, editable=False)
	roll_no = models.IntegerField(null=False)
	class_id = models.ForeignKey(Course_Class, related_name = 'student_in_class')
	student_id = models.ForeignKey(Student, related_name = 'student_in_class')
	
	class Meta:
		db_table = 'student_in_class'

class Exam(models.Model):
	exam_id = models.IntegerField(primary_key=True, editable=False)
	date = models.DateField()
	subject_id = models.ForeignKey(Subject, related_name = 'exam')

	class Meta:
		db_table = 'exam'
		
class Marks(models.Model):
	exam_id = models.ForeignKey(Exam, related_name = 'marks')
	student_class_id = models.ForeignKey(Student_in_class, related_name = 'marks')
	marks_obtained = models.IntegerField(null=False)
	marks_out_of = models.IntegerField(null=False)

	class Meta:
		db_table = 'marks'

class Attendance(models.Model):
	attendance_id = models.IntegerField(primary_key=True, editable=False)
	date = models.DateField()
	class_id = models.ForeignKey(Course_Class, related_name = 'attendance')
	attendance_data = models.TextField( null = False )

	class Meta:
		db_table = 'attendance'	


class School_user(models.Model):
	user_id = models.IntegerField (primary_key = True)
	user_name = models.CharField(max_length=70)
	password = models.CharField(max_length=70)
	is_active = models.BooleanField()
	user_type = models.IntegerField(null=False)

	class Meta:
		db_table = 'school_user'

class Parent(models.Model):	
	parent_id = models.IntegerField(primary_key=True, editable=False)
	user_id = models.ForeignKey(School_user, related_name = 'parent')
	fname = models.CharField(max_length=30, null = False)
	lname = models.CharField(max_length=30, null = False)
	contact = models.DecimalField(max_digits=10, decimal_places=0)

	class Meta:
		db_table='parent'

class Student(models.Model):
	student_id = models.IntegerField(primary_key=True, editable=False)
	user_id = models.ForeignKey(School_user, related_name='student')
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	contact = models.DecimalField(max_digits=10, decimal_places=0 )

	class Meta:
		db_table='student'

class Teacher(models.Model):
	teacher_id = models.IntegerField(primary_key=True, editable=False)
	user_id = models.ForeignKey(School_user, related_name='teacher')
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	contact = models.DecimalField(max_digits=10, decimal_places=0)

	class Meta:
		db_table = 'teacher'

