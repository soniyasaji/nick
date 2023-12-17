from django.shortcuts import render
from books.models import Book
from books.forms import BookForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')

@login_required
def add(request):   #user defined type
    if(request.method=="POST"):  #after for submission
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        f=request.FILES.get('f')
        i=request.FILES.get('i')
        b=Book.objects.create(title=t,author=a,price=p,pdf=f,image=i)
        b.save()
        return view(request)
    return render(request,'add.html')

@login_required
def viewbook(request,p):
    b=Book.objects.get(id=p)
    return render(request,'viewbook.html',{'b':b})

@login_required
def editbook(request,p):
    b=Book.objects.get(id=p)
    if (request.method == "POST"):
        form=BookForm(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return view(request)

    form=BookForm(instance=b)

    return render(request,'edit.html',{'f':form})

@login_required
def deletebook(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return view(request)

@login_required
def view(request):
    b=Book.objects.all()
    return render(request,'view.html',{'s':b})



@login_required
def factorial(request):
    if(request.method=="POST"):
        n=int(request.POST['n'])
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return render(request,'fact.html',{'f':fact})
    return render(request,'fact.html')











