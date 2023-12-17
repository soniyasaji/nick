from django.shortcuts import render
from kids.models import Kids

def addkids(request):
    return render(request,'addkids.html')


def viewkids(request):
    return render(request,'viewkids.html')


