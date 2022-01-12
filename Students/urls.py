from django.urls import path, include
from .views import * 
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('api/student' , Student_api, basename='student')
urlpatterns = [
    path('',include(router.urls))
    
    
    ]