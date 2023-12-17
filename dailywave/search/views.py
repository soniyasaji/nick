from django.shortcuts import render
from newspaper.models import News_Type
from django.db.models import Q
def searchresult(request):
    query=""
    newstype=None
    if(request.method=="POST"):
        query=request.POST['q']
        if(query):
            newstype=News_Type.objects.filter(Q(ntypname__icontains=query) | Q(ndesc__icontains=query))
    return render(request,'search.html',{'t':newstype,'q':query})
