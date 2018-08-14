class Department(models.Model):
	department_id = models.IntegerField(primary_key=True, editable=False)
	name = models.CharField(max_length=30)

	class Meta:
		db_table = 'department'

class Course(models.Model):
	course_id = models.IntegerField(primary_key=True, editable=False)
	course_name = models.CharField(max_length=30)
	department_id = models.ForeignKey(Department, related_name = 'course')
 
	class Meta:
		db_table = 'course'

class Course_Class(models.Model):
	class_id = models.IntegerField(primary_key=True, editable=False)
	course_id = models.ForeignKey(Course, related_name = 'course')
	teacher_id = models.ForeignKey(Teacher, related_name = 'course_class')
	strength = models.IntegerField(null=False)

	class Meta:
		db_table = 'couse_class'

class Subject(models.Model):
	subject_id = models.IntegerField(primary_key=True, editable=False)
	subject_name = models.CharField(max_length=30)
	class_id = models.ForeignKey(Course_Class, related_name = 'subject')
	teacher_id = models.ForeignKey(Teacher, related_name = 'subject')

	class Meta:
		db_table = 'subject'

