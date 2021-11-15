from django.db.models import fields
from django.shortcuts import render
from .models import Blog2
from django.http import HttpResponse, JsonResponse


from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import Blog2Serializer
from rest_framework import generics, status



class blog_list(APIView):
 
    @staticmethod
    def create_response(message, data, links):
        return JsonResponse({
            message,
            data,
            links,
        })


    def get(self, request, format=None):
        fields = request.query_params.get('fields', [])
        limit = request.query_params.get('limit', [])
        offset = request.query_params.get('offset', [])

        blogObjs = Blog2.objects.all()

        if limit and offset:
            start = int(offset[0])
            end = start + int(limit[0])
            blogObjs = blogObjs[start:end]

        if fields:
            fields = fields.split(',')

        serializer = Blog2Serializer(blogObjs, many=True, fields=fields)
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
