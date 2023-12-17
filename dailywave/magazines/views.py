from django.shortcuts import render
from magazines.models import Magazine

def addmag(request):
    return render(request,'addmag.html')

def viewmag(request):
    mag=Magazine.objects.all()
    return render(request,'viewmag.html',{'mag':mag})


