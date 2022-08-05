
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import datas



# Create your views here.
def home(request):
    mydata=datas.objects.all()
    if(mydata!=""):
        return render(request,'home.html',{'datas':mydata})
    else:
        return render(request,'home.html')
    

def addData(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        contact=request.POST['contact']
        address=request.POST['address']
        email=request.POST['email']

        obj=datas()
        obj.Name=name
        obj.Age=age
        obj.Contact=contact
        obj.Address=address
        obj.Email=email
        obj.save()
        mydata=datas.objects.all()
        return redirect('home')
    return render(request,'home.html')

def update(request,id):
    mydata=datas.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        contact=request.POST['contact']
        address=request.POST['address']
        email=request.POST['email']

        mydata.Name=name
        mydata.Age=age
        mydata.Contact=contact
        mydata.Address=address
        mydata.Email=email
        mydata.save()
        return redirect('home')
    return render(request,'update.html',{'data':mydata})

def delete(request,id):
    mydata=datas.objects.get(id=id)
    mydata.delete()
    return redirect('home')