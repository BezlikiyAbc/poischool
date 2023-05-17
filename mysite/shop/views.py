from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .serializers import UserSer, SchoolSer, ProductSer, CategorySer, BasketListSerializer
from .models import User, School, Product, Category
from rest_framework import viewsets
from django.db.models import Prefetch
from service_objects.services import ServiceOutcome

from .service.basket.create import BasketCreateService
from .service.basket.list import BasketListService


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


class BasketCreateListView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(BasketListService, {"user": request.user})
        return Response(BasketListSerializer(outcome.result, many=True).data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(BasketCreateService, request.POST.dict() | {"user": request.user})
        return Response(BasketListSerializer(outcome.result).data, status=status.HTTP_200_OK)
