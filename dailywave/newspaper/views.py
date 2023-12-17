from django.shortcuts import render,redirect
from newspaper.models import Newspaper,News_Type
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from newspaper.models import Video


def home(request):
    return render(request,'home.html')

def newscategory(request):
    news = Newspaper.objects.all()
    return render(request,'newscategory.html',{'news':news})
def newstype(request,news):
    t=News_Type.objects.filter(newsc__news_title=news)
    newspaper=Newspaper.objects.get(news_title=news)
    return render(request,'newstype.html',{'t':t,'newspaper':newspaper})

def newsdetails(request,t):
    nd=News_Type.objects.get(ntypname=t)
    return render(request,'newsdetails.html',{'nd':nd})

@login_required
def addnews(request):
   return render(request,'addnews.html')

@login_required
def viewnews(request):
    n=Newspaper.objects.all()
    return render(request,'viewnews.html',{'newspaper':n})

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
            return newscategory(request)
        elif (p != p1):
            messages.info(request, "Password is Incorrect")
            return redirect('login.html')
    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
            u = request.POST['u']
            p = request.POST['p']
            user = authenticate(username=u,password=p)
            if user:
                login(request,user)
                messages.info(request, "Signup Successful")
                return newscategory(request)
            else:
                messages.error(request,"Not a valid user")
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return user_login(request)

def videos(request):
    videos=Video.objects.all()
    context={
        'videos':videos,
             }
    return render(request,'videos.html',context)

def upload(request):
    if request.method == 'POST':
        title = request.POST['title']
        video = request.POST['video']

        videos = Video(title=title,video=video)
        videos.save()
        return redirect('videos')
    return render(request,'upload.html')