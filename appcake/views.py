from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from appcake.models import tbl_user,tbl_cake
from django.conf import settings
from django.core.files.storage import FileSystemStorage
def login(request):
    return render(request,'login.html')
def createuser(request):
    return render(request,'createuser.html')
def adduser(request):
    a=User()
    a.first_name=request.POST.get('firstname')
    a.username=request.POST.get('username')
    password=request.POST.get('password')
    a.set_password(password)
    a.email=request.POST.get("email")
    b=tbl_user()
    b.first_name=request.POST.get('firstname')
    b.username=request.POST.get('username')
    b.gender=request.POST.get('type')
    b.phone=request.POST.get('phone')
    b.email=request.POST.get('email')
    b.address=request.POST.get('address')
    b.photo=request.POST.get('photo')
    c=request.FILES['photo']
    fs=FileSystemStorage()
    d=fs.save(c.name,c)
    fileurl=fs.url(d)
    b.photo=fileurl
    a.save()
    b.save()
    return redirect("/")
def loginuser(request):
    uname=request.POST.get('username')
    paswd=request.POST.get('password')
    c=authenticate(username=uname,password=paswd)
    request.session['username']=uname
    if c is not None and c.is_superuser==1:
        return redirect('/admin1/')
    elif c is not None and c.is_superuser==0:
        return redirect('/user1/')
    else:
        return HttpResponse('invaliduser')
def admin2(request):
    return render(request,'admin.html')
def user2(request):
    b=request.session['username']
    c=tbl_user.objects.get(username=b)
    d=User.objects.get(username=b)
    return render(request,'user.html',{'x':b,'y':c,'n':d})

def addcake1(request):
    return render(request,'addcake.html')
def addcake4(request):
    d=tbl_cake()
    d.cakename=request.POST.get('cakename')
    d.quantity=request.POST.get('quantity')
    d.flavour=request.POST.get('flavour')
    d.price=request.POST.get('price')
    c=request.FILES['image']
    fs=FileSystemStorage()
    d1=fs.save(c.name,c)
    fileurl=fs.url(d1)
    d.image=fileurl
    d.save()
    return redirect("/addcake/")
def viewcak1(request):
    d=tbl_cake.objects.all()
    return render(request,'viewcake.html',{'data':d})
def updatecake2(request,id):
    a=tbl_cake.objects.get(id=id)
    return render(request,'updatecake.html',{'x':a})
def update5(request,id):
    try:
        a=tbl_cake.objects.get(id=id)
        a.cakename=request.POST.get('cakename')
        a.quantity=request.POST.get('quantity')
        a.flavour=request.POST.get('flavour')
        a.price=request.POST.get('price')
        # a.image=request.POST.get('image')
        c=request.FILES['image']
        fs=FileSystemStorage()
        d1=fs.save(c.name,c)
        fileurl=fs.url(d1)
        a.image=fileurl
        a.save()
    except:
        a=tbl_cake.objects.get(id=id)
        a.cakename=request.POST.get('cakename')
        a.quantity=request.POST.get('quantity')
        a.flavour=request.POST.get('flavour')
        a.price=request.POST.get('price')
        a.save() 
    return redirect('/viewcake/')
def delete1(request,id):
    a=tbl_cake.objects.get(id=id)
    a.delete()
    return redirect('/viewcake/')
def viewuser1(request):
    a=tbl_user.objects.all()
    return render(request,'viewuser.html',{'b':a})
def deleteuser2(request,id):
    a=tbl_user.objects.get(id=id)
    a.delete()
    return redirect('/viewuser/')
def cakeonly(request):
    d=tbl_cake.objects.all()
    return render(request,'viewcakeonly.html',{'data':d}) 
def profile(request):
    b=request.session['username']
    c=tbl_user.objects.get(username=b)
    d=User.objects.get(username=b)
    return render(request,'viewprofile.html',{'x':b,'y':c,'n':d})
def updateprofile1(request,id):
     a=tbl_user.objects.get(id=id)
     return render(request,'updateprofile.html',{'b':a})
def updateprofile3(request,id):
    try:
        b=tbl_user().objects.get(id=id)
        b.first_name=request.POST.get('firstname')
        b.username=request.POST.get('username')
        b.gender=request.POST.get('type')
        b.phone=request.POST.get('phone')
        b.email=request.POST.get('email')
        b.address=request.POST.get('address')
        # b.photo=request.POST.get('photo')
        c=request.FILES['photo']
        fs=FileSystemStorage()
        d=fs.save(c.name,c)
        fileurl=fs.url(d)
        b.photo=fileurl
        b.save()
    except:
        b=tbl_user.objects.get(id=id)
        b.first_name=request.POST.get('firstname')
        b.username=request.POST.get('username')
        b.gender=request.POST.get('type')
        b.phone=request.POST.get('phone')
        b.email=request.POST.get('email')
        b.address=request.POST.get('address')
        b.save()
    return redirect('/viewprofile/')
def choco(request):
    # a=tbl_cake.objects.filter(flavour="chocolates")
    a=tbl_cake.objects.filter(flavour="chocolate")

    return render(request,'chocolatecake.html',{'data':a})
def price1(request):
    a=tbl_cake.objects.filter(price__gte=1000)
    return render(request,'chocolatecake.html',{'data':a})
def back1(request):
    return render(request,'user.html')


   




    






    

# Create your views here.
