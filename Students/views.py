from .serializers import * 
from .models import * 
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import( 
                    IsAuthenticated,
                    IsAuthenticatedOrReadOnly,
                    AllowAny,
                    IsAdminUser,
                    )
from rest_framework.response import Response

from .customPermission import CustomPermission
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.throttling import (
                    UserRateThrottle,
                    AnonRateThrottle,
                    ScopedRateThrottle,
                    ) 
from rest_framework.generics import ListAPIView 
# from django_filters.rest_framework import DjangoFilterBackend


class Student_api(ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerialize
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewAll'
    filter_backends = [OrderingFilter,SearchFilter] #Using searchfilter and orderingfilter backend same time
    ordering = '-rollno'  # Default Ordering 
    filterset_fields = ['name']
    search_fields = ['^name']
