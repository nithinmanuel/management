from rest_framework import serializers
from rest_framework import fields
from rest_framework.validators import UniqueTogetherValidator
from management import models
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    employee_category_name = serializers.CharField(source = 'employee_category.employee_category_name', read_only=True)
    #owner = serializers.ReadOnlyField(source = 'owner.username') , the owner should assign with a class
    owner = serializers.CharField(source = 'owner.username', read_only=True )

    class Meta:
        model = models.Employee

        #fields = "__all__"

        fields = ['employee_name', 'date_of_birth', 'employee_age','employee_category', 'employee_category_name','owner',]

        validators = [UniqueTogetherValidator(queryset=models.Employee.objects.all(),  fields = ['employee_name', 'date_of_birth', 'employee_age','employee_category','employee_category_name',])]


class EmployeeCategorySerializer(serializers.ModelSerializer):

    employees  = serializers.StringRelatedField(many=True, read_only = True)

    class Meta:
        model = models.EmployeeCategory
        fields = ['employee_category_name', 'employees']
        validators = [UniqueTogetherValidator(queryset=models.EmployeeCategory.objects.all(),  fields=[ 'employee_category_name', 'employees',])]
class UserSerializer(serializers.ModelSerializer):
    employees  = serializers.StringRelatedField(many=True, read_only = True)

    class Meta:
        model = User
        fields = ['username', 'pk','employees']



