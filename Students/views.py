from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .serializers import * 
from .models import * 
import io  ,json
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


def show_student(request):
    if request.method == 'GET':
        json_data = request.body  
        pythonData = json.loads(json_data)
        if pythonData['id']: 
            id = pythonData['id'] 
            try:
                instance = get_object_or_404(StudentModel,pk=id) 
                serialzed = StudentSerialize(instance, many=False)
                return JsonResponse(serialzed.data)
            except StudentModel.DoesNotExist:
                pass
        instance = StudentModel.objects.all()  
        serialzed = StudentSerialize(instance,many=True)
        return JsonResponse(serialzed.data,safe=False)
    return JsonResponse('dkdjdfd',safe=False)

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body 
        pythonData = json.loads(json_data)
        serialzed = StudentSerialize(data=pythonData)
        if serialzed.is_valid():
            serialzed.save()
            return JsonResponse("Student is succefully added!. ",safe=False)
        return JsonResponse(serialzed.errors,safe=False)

@csrf_exempt
def update_student(request):
    if request.method == 'PUT':
        json_data = request.body 
        pythonData = json.loads(json_data)
        instance = StudentModel.objects.get(pk=pythonData['id'])
        serialzed = StudentSerialize(instance, data=pythonData,partial=True)
        if serialzed.is_valid():
            serialzed.save()
            return JsonResponse("Student is succefully updated!. ",safe=False)
        return JsonResponse(serialzed.errors,safe=False)

@csrf_exempt
def delete_student(request):
    if request.method == 'DELETE':
        json_data = request.body 
        pythonData = json.loads(json_data)
        try:
            StudentModel.objects.get(pk=pythonData['id']).delete()
            return JsonResponse("Student is succefully deleted!. ",safe=False)
        except StudentModel.DoesNotExist:
            return JsonResponse("Student Do Not Exist!. ",safe=False)

