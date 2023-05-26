from django.urls import path
from loginapp import views
from .views import *

urlpatterns = [
    path('',views.loginprofile,name='login profile'),
    path('t/',views.teacher,name='teacher login')

    ]