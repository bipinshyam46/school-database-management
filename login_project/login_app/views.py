from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control





# Create your views here.
def home(request):
    return render(request,'about.html')

def register(request):
    return render(request,'register.html')

def studentreg(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']

        User.objects.create_user(name=name,dob=dob,username=username,password=password,phone=phone,is_staff=0,is_active=1)
        return redirect(register)

    else:
        return render(request,'studentreg.html')

def teacherreg(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']

        User.objects.create_user(name=name,dob=dob,username=username,password=password,phone=phone,is_staff=1,is_active=1)
        return redirect(register)

    else:
        return render(request,'teacherreg.html')

@login_required(login_url='login')
def studentprofile(request):

    id=request.session['st_id']
    
    st=User.objects.filter(is_active=1,is_staff=0,is_superuser=0,id=id)
    return render(request,'studentprofile.html',{'st':st})

@login_required(login_url='login')
def teacherprofile(request):
    
    id=request.session['tch_id']
    tch=User.objects.filter(is_active=1,is_staff=1,is_superuser=0,id=id)

    return render(request,'teacherprofile.html',{'tch':tch})
    



def Login(request):
    message=''
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user is not None:
            if user.is_superuser==1:
                login(request,user)
                return redirect(admin)
            
            elif user.is_active==1 and user.is_staff==0:
                login(request,user)
                request.session['st_id']=user.id
                return redirect(studentprofile)
            elif user.is_active==1 and user.is_staff==1:
                login(request,user)
                request.session['tch_id']=user.id
                return redirect(teacherprofile)
        else:
            message='Invalid Credentials'

            return render(request,'about.html',{'message':message})
    else:
        return render(request,'about.html')

@cache_control(no_cache=True, must_revalidate=True)
def Logout(request):
    auth.logout(request)
    request.session.flush()
    return redirect(Login)

def admin(request):
    return render(request,'admin.html')

@login_required(login_url='login')
def teacherview(request):
    # id=request.session['tch_id']
    tch=User.objects.filter(is_active=1,is_staff=1,is_superuser=0)

    return render(request,'teacherview.html',{'tch':tch})

@login_required(login_url='login')



def studentview(request):
    # id=request.session['tch_id']
    st=User.objects.filter(is_active=1,is_staff=0)

    return render(request,'studentview.html',{'st':st})

@login_required(login_url='login')
def editteacher(request):
    id=request.session['tch_id']
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        phone=request.POST['phone']
        username=request.POST['username']
        data=User.objects.filter(id=id)
        data.update(name=name,username=username,phone=phone,dob=dob)
        # .update(name=name,username=username,phone=phone,dob=dob)
        # User.objects.create_user(name=name,username=username,phone=phone,dob=dob)
        return redirect(teacherprofile)

        
    else:
        id=request.session['tch_id']
        tch=User.objects.filter(is_active=1,is_staff=1,is_superuser=0,id=id)
        return render(request,'editteacher.html',{'tch':tch})

@login_required(login_url='Login')
def editstudent(request):
    id=request.session['st_id']
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        phone=request.POST['phone']
        username=request.POST['username']
        a=User.objects.filter(id=id)
        a.update(name=name,username=username,phone=phone,dob=dob)
        return redirect(studentprofile)

        
    else:
        id=request.session['st_id']
        st=User.objects.filter(is_active=1,is_staff=0,is_superuser=0,id=id)
        return render(request,'editstudent.html',{'st':st})
    
