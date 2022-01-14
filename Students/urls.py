from django.urls import path, include
from .views import * 
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('api/student' , Student_api, basename='student')
urlpatterns = [
    path('',include(router.urls)),
    # path('home/',include('rest_framework.urls'), name='rest_framework_url')
    
    ]