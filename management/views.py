from django.shortcuts import render
from rest_framework import generics
from management import models
from .import serializers
from rest_framework import permissions
from management import custompermission
from management.custompermission import IsCurrentUserOwnerOrReadOnly
from django.contrib.auth.models import User
from management.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ListEmployeeCategory(generics.ListCreateAPIView):
    queryset = models.EmployeeCategory.objects.all()
    serializer_class = serializers.EmployeeCategorySerializer
class DetailEmployeeCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EmployeeCategory.objects.all()
    serializer_class = serializers.EmployeeCategorySerializer

class ListEmployee(generics.ListCreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, custompermission.IsCurrentUserOwnerOrReadOnly,)

class DetailEmployee(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeCategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, custompermission.IsCurrentUserOwnerOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer








# Create your views here.
