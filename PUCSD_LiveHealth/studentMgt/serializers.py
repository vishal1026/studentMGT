from rest_framework import serializers
from models import *

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_user
        fields = '__all__'
class parentSerializer(serializers.ModelSerializer):
    user_id = userSerializer()
    class Meta:
        model = School_user
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

class teacherSerializer(serializers.ModelSerializer):
    user_id = userSerializer()
    class Meta:
        model = Teacher
        fields = '__all__'

class courseclassSerializer(serializers.ModelSerializer):
    teacher_id = teacherSerializer()
    course_id = courseSerializer()
    class Meta:
        model = Course_Class
        fields = '__all__'


class attendanceSerializer(serializers.ModelSerializer):
    class_id = courseclassSerializer()
    class Meta:
        model = Attendance
        fields = '__all__'

class studentSerializer(serializers.ModelSerializer):
    user_id = userSerializer()
    parent_id=parentSerializer()
    class Meta:
        model = Student
        fields = '__all__'
