import datetime
from datetime import datetime

import requests

from PIL import Image
from django.http import JsonResponse
from django.conf import settings
from datetime import timedelta
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.utils.timezone import localtime
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from rest_framework import status, serializers
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action, api_view
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from task.models import Task, TaskHistory
from django.shortcuts import render
from users.models import UserCustomer
from users.serializers import UserCustomerSerializer, UserCustomerListSerializer
# Create your views here.

class UserCustomerViewSet(ModelViewSet):
    #permission_classes = (IsAppAuthenticated, IsAppStaff, IsAuthenticated, IsSuperUser)
    queryset = UserCustomer.objects.all()
    serializer_class = UserCustomerListSerializer
    filter_backends = (DjangoFilterBackend,)
    #filter_fields = ('is_enabled',)


    def create(self, request, *args, **kwargs):
        serializer = UserCustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data.get('password'))
            serializer.save()
            return Response(UserCustomerListSerializer(instance=serializer.instance).data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        company = self.get_object()
        serializer = UserCustomerSerializer(company, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data.get('password'))
            serializer.save()

            return Response(UserCustomerListSerializer(instance=serializer.instance).data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)