from rest_framework import serializers
from models import *

class school_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_user
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