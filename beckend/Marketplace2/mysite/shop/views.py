from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .serializers import UserSer, SchoolSer, ProductSer, CategorySer
from .models import User, School, Product, Category
from rest_framework import viewsets
from django.db.models import Prefetch

class UsersListAll(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSer(users, many=True)
        return Response(serializer.data)
    
class SchooListAll(APIView):
    def get(self, request, format=None):
        schools = School.objects.all()
        serializer = SchoolSer(schools, many=True)
        return Response(serializer.data)