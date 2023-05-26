from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name=models.CharField(max_length=30,blank=False,verbose_name='Name')
    dob=models.DateField(blank=False,verbose_name='DOB',default='2000-12-08')
    phone=models.IntegerField(blank=False,verbose_name='Phone number',null=True)
    class Meta:
        db_table='Usertable'