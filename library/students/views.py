from django.shortcuts import render,redirect
from students.models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        p1=request.POST['p1']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        if(p==p1):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return redirect('books:home')

    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            messages.error(request,"Invalid credentials")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)

@login_required
def studentdetails(request):
    s=Student.objects.all()
    return render(request,'details.html',{'st':s})


