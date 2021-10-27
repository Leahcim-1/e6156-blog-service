from django.shortcuts import render
from .models import Test, Blog2

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import TestSerializer, Blog2Serializer

# Create your views here.

class Test(viewsets.ModelViewSet):
    queryset=Test.objects.all()
    serializer_class=TestSerializer
    
    def post(self, request):
        name=request.POST.get('name')

class Blog2(viewsets.ModelViewSet):
    queryset=Blog2.objects.all()
    serializer_class=Blog2Serializer
    
    def post(self, request):
        name=request.POST.get('title','body','user_id','tag','create_time', 'update_time')