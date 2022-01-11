from django.urls import path
from .views import * 
urlpatterns = [

    path('api/student/',Student_api.as_view()),
    path('api/student/<int:id>/',Student_api.as_view())
    
    
    ]