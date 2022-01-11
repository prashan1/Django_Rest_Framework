from django.urls import path
from .views import * 
urlpatterns = [
    
    # path("students/", students) , 
    # path('student/<int:pk>/', student),
    # path('create-student/', createStudent)
    path('show-student/',show_student),
    path('create-student/',create_student),
    path('udpate-student/',update_student),
    path('delete-student/',delete_student)
    
    
    ]