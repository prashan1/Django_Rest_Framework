from .serializers import * 
from .models import * 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
                ListModelMixin,
                RetrieveModelMixin,
                CreateModelMixin,
                UpdateModelMixin,
                DestroyModelMixin,
            )

#Aggregating api which don't require pk and have common memebers
class Student_api_LC(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = StudentModel.objects.all()  
    serializer_class = StudentSerialize

    def get(self, request, *args, **kwargs):
        return self.list( request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create( request, *args, **kwargs)

class Student_api_RUD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin ):
    queryset = StudentModel.objects.all()  
    serializer_class = StudentSerialize

    def get(self, request, *args, **kwargs):
        return self.retrieve( request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update( request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy( request, *args, **kwargs)