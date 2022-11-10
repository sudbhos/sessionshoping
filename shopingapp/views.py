from django.shortcuts import render
from .forms import addi
# Create your views here.

def additm(request):
    form=addi()
    if request.method=="POST":
        name=request.POST['name']
        quentity=request.POST['quentity']
        request.session[name]=quentity
    return render(request, "testapp/additem.html",{"form":form})

def desply(request):
    return render(request,"testapp/display.html")