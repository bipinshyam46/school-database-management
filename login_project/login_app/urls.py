from login_app import views
from django.urls import path
from .views import *


urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('studentreg',views.studentreg,name='studentreg'),
    path('teacherreg',views.teacherreg,name='teacherreg'),
    path('studentprofile',views.studentprofile,name='studentprofile'),
    path('teacherprofile',views.teacherprofile,name='teacherprofile'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('admin',views.admin,name='admin'),
    path('teacherview',views.teacherview,name='teacherview'),
    path('studentview',views.studentview,name='studentview'),
    path('editteacher',views.editteacher,name='editteacher'),
    path('editstudent',views.editstudent,name='editstudent')
    
]
