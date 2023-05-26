from django.shortcuts import render

def loginprofile(request):
    return render(request,'login.html')

def teacher(request):
    return render(request,'teacher.html')