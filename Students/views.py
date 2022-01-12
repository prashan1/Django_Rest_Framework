from .serializers import * 
from .models import * 
from rest_framework import viewsets

#Aggregating api which don't require pk and have common memebers
class Student_api(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerialize
