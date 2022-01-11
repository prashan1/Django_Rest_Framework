from django.contrib import admin
from .models import * 
@admin.register(StudentModel)
class CustomAdmin(admin.ModelAdmin):
    list_display=['id','name','age','rollno']
# Register your models here.
