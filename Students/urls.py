from django.urls import path
from .views import * 
urlpatterns = [

    path('api/student/',Student_api_LC.as_view()),
    path('api/student/<int:pk>/',Student_api_RUD.as_view())
    
    
    ]