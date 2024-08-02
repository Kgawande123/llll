from django.shortcuts import render,redirect
from .forms import CarForm
from .models import Car

# Create your views here.
def cview(request):
    form = CarForm()
    if request.method == "POST":
        form =CarForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect("/a1/sv/")
    return  render(request,"app1/car.html",{"form":form})


def sview(request):
    obj = Car.objects.all()
    return render(request,"app1/show.html",{"obj":obj})

def hview(request):
    return render(request,"app1/home.html",{})

def uview(request,pk):
    obj = Car.objects.get(cid=pk)
    form = CarForm( instance=obj)
    if request.method == "POST":
        form =CarForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return  redirect("/a1/sv/")
    return  render(request,"app1/car.html",{"form":form})

def dview(request,k):
    obj = Car.objects.get(cid=k)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/success.html",{"obj":obj})
