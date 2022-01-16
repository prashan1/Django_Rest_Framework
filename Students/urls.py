from django.urls import path, include
from .views import * 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
                                            TokenObtainPairView, 
                                            TokenRefreshView, 
                                            TokenVerifyView 
                                        )

router = DefaultRouter()
router.register('api/student' , Student_api, basename='student')
urlpatterns = [
    path('',include(router.urls)),
    path('home/',include('rest_framework.urls'), name='rest_framework_url'),
    path('gettoken/',TokenObtainPairView.as_view()),
    path('refreshtoken/',TokenRefreshView.as_view()),
    path('verifytoken/',TokenVerifyView.as_view()),
    
    ]