from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    rollno = models.IntegerField()

    def __str__(self):
        return self.name
