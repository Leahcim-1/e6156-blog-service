from django.db.models import fields
from django.shortcuts import render
from .models import Blog2
from django.http import HttpResponse, JsonResponse
import time

from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import Blog2Serializer
from rest_framework import generics, status



class blog_list(APIView):
 
    @staticmethod
    def create_response(message, data, links):
        return {
            "message": message,
            "data": data,
            "links": links,
        }
    
    @staticmethod
    def get_links(limit, offset):
        query_str = "limit=%s&offset=%s"
        cur = query_str % (limit, offset)
        next = query_str % (limit, offset + limit)
        prev = query_str % (limit, offset - limit) if offset >= limit else ""

        return {
            "cur": cur,
            "prev": prev,
            "next": next,
        }



    def get(self, request, format=None):
        fields = request.query_params.get('fields', [])
        limit = request.query_params.get('limit', [])
        offset = request.query_params.get('offset', [])

        print(limit, offset)

        blogObjs = Blog2.objects.all()

        links = []
        if limit and offset:
            ofs = int(offset)
            lim = int(limit)
            start = ofs
            end = start + lim
            blogObjs = blogObjs[start:end]
            page = blog_list.get_links(lim, ofs)
            links = [
                {
                    "rel": "cur",
                    "link": request.path + "?" + page.get('cur')
                },
                {
                    "rel": "next",
                    "link": request.path + "?" + page.get('next')
                },
            ]
            if ofs >= lim:
                links.append({
                    "rel": "prev",
                    "link": request.path + "?" + page.get('prev')
                })

        if fields:
            fields = fields.split(',')

        serializer = Blog2Serializer(blogObjs, many=True, fields=tuple(fields))

        res = blog_list.create_response(
            message = "OK",
            data = serializer.data,
            links = links
        )
        return Response(res)

    def post(self, request, format=None):
        data = request.data
        data['create_time'] = int(time.time() * 1000)
        data['update_time'] = int(time.time() * 1000)
        serializer = Blog2Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class blog_detail(APIView):

    @staticmethod
    def create_response(message, data, links):
        return {
            "message": message,
            "data": data,
            "links": links,
        }

    def get_object(self, pk):
        try:
            return Blog2.objects.get(pk=pk)
        except Blog2.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        this_blog = self.get_object(pk)
        serializer = Blog2Serializer(this_blog)
        res = blog_detail.create_response("OK", [serializer.data], [])
        return Response(res)

    def put(self, request, pk, format=None):
        this_blog = self.get_object(pk)
        data=request.data
        data['update_time'] = int(time.time() * 1000)
        serializer = Blog2Serializer(this_blog, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        this_blog = self.get_object(pk)
        this_blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
