from django.shortcuts import render
from .models import Blog2
from django.http import HttpResponse, JsonResponse


from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import Blog2Serializer
from rest_framework import generics, status
import django_filters.rest_framework



class blog_list(APIView):

    def get(self, request, format=None):
        blogObjs = Blog2.objects.all()
        serializer = Blog2Serializer(blogObjs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Blog2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class blog_detail(APIView):

    def get_object(self, pk):
        try:
            return Blog2.objects.get(pk=pk)
        except Blog2.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        this_blog = self.get_object(pk)
        serializer = Blog2Serializer(this_blog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        this_blog = self.get_object(pk)
        serializer = Blog2Serializer(this_blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        this_blog = self.get_object(pk)
        this_blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
