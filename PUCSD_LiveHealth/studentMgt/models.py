# * coding: utf8 *
from __future__ import unicode_literals

from django.db import models

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

