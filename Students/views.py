from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .serializers import * 
from .models import * 
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view   

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request, id=None):
    if request.method == 'GET':
        if id is not None:
            instance = get_object_or_404(StudentModel,pk=id) 
            serialzed = StudentSerialize(instance, many=False)
            return Response(serialzed.data)
        instance = StudentModel.objects.all()  
        serialzed = StudentSerialize(instance,many=True)
        return Response(serialzed.data)

    if request.method == 'POST':
        serialzed = StudentSerialize(data = request.data)
        if serialzed.is_valid():
            serialzed.save()
            return Response("Student is succefully added!. ")
        return Response(serialzed.errors)
    if request.method == 'PUT':
        instance = get_object_or_404(StudentModel,pk=id) 
        serialzed = StudentSerialize(instance, data = request.data)
        if serialzed.is_valid():
            serialzed.save()
            return Response("Student is succefully updated!. ")
        return Response(serialzed.errors)
    if request.method == 'PATCH':
        instance = get_object_or_404(StudentModel,pk=id) 
        serialzed = StudentSerialize(instance, data = request.data,partial=True)
        if serialzed.is_valid():
            serialzed.save()
            return Response("Student is succefully updated!. ")
        return Response(serialzed.errors)
    if request.method == 'DELETE':
        get_object_or_404(StudentModel,pk=id).delete()
        return Response("Student is succefully deleted!. ")