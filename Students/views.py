from .serializers import * 
from .models import * 
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import( 
                    IsAuthenticated,
                    IsAuthenticatedOrReadOnly,
                    AllowAny
                    )
from .customPermission import CustomPermission
from rest_framework.filters import OrderingFilter
from rest_framework.throttling import (
                    UserRateThrottle,
                    AnonRateThrottle
                    ) 
from .throttling import CustomUserThrottle

class Student_api(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerialize
    authentication_classes = [SessionAuthentication]
    permisssion_classes =[IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle,AnonRateThrottle]
    filter_backends  =[OrderingFilter]
    ordering_fields= ['name']
    # throttle_classes = [CustomUserThrottle,AnonRateThrottle]
    # authentication_classes = [BasicAuthentication]
    # permisssion_classes =[CustomPermission]
    # permisssion_classes =[AllowAny]
