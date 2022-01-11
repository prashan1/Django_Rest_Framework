from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .serializers import * 
from .models import * 
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

class Student_api(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            instance = get_object_or_404(StudentModel,pk=id) 
            serialzed = StudentSerialize(instance, many=False)
            return Response(serialzed.data)
        instance = StudentModel.objects.all()  
        serialzed = StudentSerialize(instance,many=True)
        return Response(serialzed.data)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        serialzed = StudentSerialize(data = request.data)
        if serialzed.is_valid():
            serialzed.save()
            return Response("Student is succefully added!. ")
        return Response(serialzed.errors, status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        instance = get_object_or_404(StudentModel,pk=id) 
        serialzed = StudentSerialize(instance, data = request.data)
        if serialzed.is_valid():
            serialzed.save()
            return Response("Student is succefully updated!. ")
        return Response(serialzed.errors, status = status.HTTP_400_BAD_REQUEST)
    def patch(self, request, *args, **kwargs):
        id = kwargs.get('id')
        instance = get_object_or_404(StudentModel,pk=id) 
        serialzed = StudentSerialize(instance, data = request.data,partial=True)
        if serialzed.is_valid():
            serialzed.save()
            return Response("Student is succefully updated!. ")
        return Response(serialzed.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        get_object_or_404(StudentModel,pk=id).delete()
        return Response("Student is succefully deleted!. ")