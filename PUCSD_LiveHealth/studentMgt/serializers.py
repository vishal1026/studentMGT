from rest_framework import serializers
from models import *

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class courseSerializer(serializers.ModelSerializer):
    department_id = departmentSerializer()
    class Meta:
        model = Course
        fields = '__all__'
