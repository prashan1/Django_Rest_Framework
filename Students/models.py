from django.db import models
from django.conf import settings
from django.dispatch import receiver 
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    rollno = models.IntegerField()

    def __str__(self):
        return self.name
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,created=False,instance=None,**kwargs):
    if created:
        Token.objects.create(user=instance)
