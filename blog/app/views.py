from django.shortcuts import render
from .models import Test, Blog2
from django.http import HttpResponse, JsonResponse


from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import TestSerializer, Blog2Serializer
from rest_framework import generics, status
import django_filters.rest_framework



class test_list(APIView):

    def get(self, request, format=None):
        testObjs = Test.objects.all()
        serializer = TestSerializer(testObjs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class test_detail(APIView):

    def get_object(self, pk):
        try:
            return Test.objects.get(pk=pk)
        except Test.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        this_test = self.get_object(pk)
        serializer = TestSerializer(this_test)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        this_test = self.get_object(pk)
        serializer = TestSerializer(this_test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        this_test = self.get_object(pk)
        this_test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Blog2View(viewsets.ModelViewSet):
    queryset=Blog2.objects.all()
    serializer_class=Blog2Serializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    
    def post(self, request):
        name=request.POST.get('title','body','user_id','tag','create_time', 'update_time')

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Blog2.objects.all()
        return queryset