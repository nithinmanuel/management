from django.db import models
from django.contrib.auth.models import User

class EmployeeCategory(models.Model):
    employee_category_name = models.CharField(max_length = 256)
    class Meta():
        ordering = ('employee_category_name',)
        def __str__(self):
            return (self.employee_category_name)
class Employee(models.Model):
    employee_category = models.ForeignKey(EmployeeCategory, related_name = 'employees', on_delete = models.CASCADE)
    employee_name = models.CharField(max_length = 256)
    date_of_birth = models.DateField()
    employee_age = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name = 'employees', on_delete = models.CASCADE)
    #employee_photo = models.ImageField()
    class Meta():
        ordering = ('employee_name',)
        def __str__(self):
            return (self.employee_name)

# Create your models here.
