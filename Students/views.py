from .serializers import * 
from .models import * 
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
                                IsAuthenticated,
                                AllowAny
)

#Aggregating api which don't require pk and have common memebers
class Student_api(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerialize
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    
