from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from .models import user2
import re
# Create your views here.
def isValid(str):
    regex = ("^(?=.*[a-z])(?=." +
             "*[A-Z])(?=.*\\d)" +          #checks if password has atlast 1 uppercase character, 1 lowercase character, 1 special character, 1 numeric character
             "(?=.*[-+_!@#$%^&*., ?]).+$")
     
    p = re.compile(regex)

    if(re.search(p, str)):
        return True
    else:
       return False

def index(request):
    if not request.user.is_authenticated:
        return render(request,"users/login.html",{'message':"You need to sign in to access that page",'code':"danger"})
    else:
        data=user2.objects.filter(user=request.user)
        print(messages)
        return render(request,"users/index.html",{'data':data})

def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"users/login.html",{'message':"Invalid Credentials.",'code':"danger"})
    return render(request,"users/login.html")

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        Gender=request.POST['Gender']
        age=request.POST['age']
        phonenum=request.POST['phonenumber']
        if User.objects.filter(username=username).exists():
            return render(request,"users/register.html",{'message':"Username already exists",'code':"danger"})
        if User.objects.filter(email=email).exists():
            return render(request,"users/register.html",{'message':"Email is already used",'code':"danger"})
        if user2.objects.filter(phonenum=phonenum).exists():
            return render(request,"users/register.html",{'message':"Number is already used",'code':"danger"})
        if(len(password1)<8):
            return render(request,"users/register.html",{'message':"Password should have greater than 8 characters",'code':"danger"})
        if not isValid(password1):
            return render(request,"users/register.html",{'message':"Password is not strong enough",'code':"danger"})
        if(password1!=password2):
            return render(request,"users/login.html",{'message':"Passwords don't match",'code':"danger"})
        user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password1,last_name=last_name)
        newuser=user2(gender=Gender,age=age,phonenum=phonenum,user=user)
        user.save()
        newuser.save()
        print("success")
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request,"users/register.html")

def search(request):
    data=None
    check=False
    if(request.method=='GET'):
        sEmail=request.GET.get('semail')
        
        if User.objects.filter(email=sEmail).exists():
            data=User.objects.filter(email=sEmail)
            usertemp=data.get()
            data2=user2.objects.filter(user=usertemp)
            return render(request,"users/search.html",{"user1":data,"user2":data2})
        else:
            check=True
            return render(request,"users/search.html",{"message":"User not found! ):","found":check})
    else:
        return render(request,"users/search.html")


def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{'message':"Logged out successfully",'code':"success"})
