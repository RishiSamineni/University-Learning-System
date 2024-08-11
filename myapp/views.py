from django.shortcuts import render
from .models import *
# Create your views here.

#View for Register page

def RegisterPage(request):
    return render(request,"app/register.html")

def UserRegister(request):
    if request.method == "POST":
        Username = request.POST['Username']
        Email  =  request.POST['email']
        Password =  request.POST['password']
        Confirm_Password  = request.POST['cpassword']
        user =  User.objects.filter(Email=Email)
        
        if user:
            message = "User already exist"
            return render(request,"app/register.html",{'msg':message})
        else:
            if Password == Confirm_Password:
                newuser = User.objects.create(Username=Username,Email=Email,Password=Password,Confirm_Password=Confirm_Password)
                message =  "User Register success"
                return render(request,"app/login.html",{'msg':message})
            else:
                message = "Password and Confirm Password does not match"
                return render(request,"app/register.html",{'msg':message})
                
                