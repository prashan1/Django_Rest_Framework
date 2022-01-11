from .serializers import * 
from .models import * 
from rest_framework.generics import (
                ListCreateAPIView,
                RetrieveUpdateDestroyAPIView,
            )

#Aggregating api which don't require pk and have common memebers
class Student_api_LC(ListCreateAPIView):
    queryset = StudentModel.objects.all()  
    serializer_class = StudentSerialize

class Student_api_RUD(RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()  
    serializer_class = StudentSerialize