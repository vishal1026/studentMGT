# * coding: utf8 *
from __future__ import unicode_literals

from django.db import models

class School_user(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=70, unique = True)
	password = models.CharField(max_length=70)
	is_active = models.BooleanField( default = True )
	user_type = models.IntegerField(null=False)
	
	class Meta:
		db_table = 'school_user'

class Parent(models.Model):	
	parent_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(School_user, related_name = 'parent')
	fname = models.CharField(max_length=30, null = False)
	lname = models.CharField(max_length=30, null = False)
	contact = models.DecimalField(max_digits=10, decimal_places=0)

	class Meta:
		db_table='parent'
	
class Student(models.Model):
	student_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(School_user, related_name='student')
	parent_id = models.ForeignKey(Parent, related_name='student')
	fname = models.CharField(max_length=30, null= False)
	lname = models.CharField(max_length=30, null=False)
	contact = models.DecimalField(max_digits=10, decimal_places=0 )

	class Meta:
		db_table='student'

class Teacher(models.Model):
	teacher_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(School_user, related_name='teacher')
	fname = models.CharField(max_length=30, null= False)
	lname = models.CharField(max_length=30, null= False)
	contact = models.DecimalField(max_digits=10, decimal_places=0)

	class Meta:
		db_table = 'teacher'

class Department(models.Model):
	department_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30, null=False, unique = True)

	class Meta:
		db_table = 'department'

class Course(models.Model):
	course_id = models.AutoField(primary_key=True)
	course_name = models.CharField(max_length=30,null=False, unique=True)
	department_id = models.ForeignKey(Department, related_name = 'course')
 
	class Meta:
		db_table = 'course'

class Course_Class(models.Model):
	class_id = models.AutoField(primary_key=True)
	course_id = models.ForeignKey(Course, related_name = 'course')
	teacher_id = models.ForeignKey(Teacher, null=False,  related_name = 'course_class')
	strength = models.IntegerField(null=False)

	class Meta:
		db_table = 'couse_class'

class Subject(models.Model):
	subject_id = models.AutoField(primary_key=True)
	subject_name = models.CharField(max_length=30,null=False)
	class_id = models.ForeignKey(Course_Class, related_name = 'subject')
	teacher_id = models.ForeignKey(Teacher, related_name = 'subject')

	class Meta:
		db_table = 'subject'

class Student_in_class(models.Model):
	student_class_id = models.AutoField(primary_key=True)
	roll_no = models.IntegerField(null=False)
	class_id = models.ForeignKey(Course_Class, related_name = 'student_in_class')
	student_id = models.ForeignKey(Student, related_name = 'student_in_class')
	
	class Meta:
		db_table = 'student_in_class'

class Exam(models.Model):
	exam_id = models.AutoField(primary_key=True)
	exam_name = models.CharField(null=False,max_length=20) 
	date = models.DateTimeField(null=False)
	subject_id = models.ForeignKey(Subject, null=False, related_name = 'exam')

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
	attendance_id = models.AutoField(primary_key=True)
	date = models.DateField(null=False)
	class_id = models.ForeignKey(Course_Class, related_name = 'attendance')
	attendance_data = models.TextField( null = False )

	class Meta:
		db_table = 'attendance'