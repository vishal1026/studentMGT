from rest_framework import serializers
from models import *

class school_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_user
        fields = '__all__'


class parentSerializer(serializers.ModelSerializer):
    user_id = school_userSerializer()
    class Meta:
        model = Parent
        fields = '__all__'


class studentSerializer(serializers.ModelSerializer):
    user_id= school_userSerializer()
    class Meta:
        model = Student
        fields = '__all__'


class teacherSerializer(serializers.ModelSerializer):
    user_id = school_userSerializer()
    class Meta:
        model = Teacher
        fields = '__all__'


class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class courseSerializer(serializers.ModelSerializer):
    department_id = departmentSerializer()
    class Meta:
        model = Course
        fields = '__all__'

class course_ClassSerializer(serializers.ModelSerializer):
    course_id = courseSerializer()
    teacher_id = teacherSerializer()
    class Meta:
        model = Course_Class
        fields = '__all__'

    
class student_in_classSerializer(serializers.ModelSerializer):
    student_id = studentSerializer()
    class_id = course_ClassSerializer()
    class Meta:
        model = Student_in_class
        fields = '__all__'