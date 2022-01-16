from .serializers import * 
from .models import * 
from rest_framework import viewsets
from rest_framework.permissions import (
                                IsAuthenticated,
                                AllowAny
)
from rest_framework.pagination import PageNumberPagination
#Using JWT authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
class Student_api(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerialize
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny] 
    # pagination_classes = [PageNumberPagination]

    
