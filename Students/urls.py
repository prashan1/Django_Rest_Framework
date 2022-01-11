from django.urls import path
from .views import * 
urlpatterns = [

    path('api/student/',student_api),
    path('api/student/<int:id>/',student_api)
    
    
    ]