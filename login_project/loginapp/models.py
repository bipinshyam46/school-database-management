from __future__ import division
from msilib.schema import Class
from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=50,verbose_name='Student name')
    std=models.IntegerField(verbose_name='Class')
    division=models.CharField(max_length=3,verbose_name='Division')
    dob=models.DateField(verbose_name='DOB')

class Teacher(models.Model):
    name=models.CharField(max_length=50,verbose_name='Name')
    age=models.IntegerField(verbose_name='Age')
    subject=models.CharField(max_length=50,verbose_name='Subject')





    
    
