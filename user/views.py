from django.shortcuts import render,redirect

#For Authentification
from django.contrib.auth import authenticate,login ,logout
#For pop up Messages
from django.contrib import messages
#To register we import
from django.contrib.auth.models import User

#Importing form
from .forms import studentform
from django.http import HttpResponseRedirect
from  .models import Studentdetails






def profile(request):
        submitted =False
        
        if request.method=="POST":
            form =studentform(request.POST,request.FILES)
            if form.is_valid():
                form.save()

                return HttpResponseRedirect("/profile?submitted=True")
        else:
            form =studentform
            if 'submitted' in request.GET:
                submitted =True
            
        name=request.user
        
        
        return render(request,'profile.html',{
        'user':name,
        'form':form,
        'submitted':submitted,
    })


def index(request):
    
    return render(request,'welcome.html',{
        
    })

def dashboard(request):
    user_details =Studentdetails.objects.all()
    return render(request,'dashboard.html',{
        "details":user_details,
    })



def login_user(request):
    if request.method =="POST":
        username =request.POST.get("user")
        password =request.POST.get("password")

        user =authenticate(request,username =username , password =password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been logged in Successfully!!!!!!')

            return redirect('profile')
            
        else:
            messages.success(request,'There was an error when logging in,Please Login in again!!!!!')
            
            return redirect('login')
        
    else:
        return render(request,'login.html',{})


def logout_user(request):
    
    logout(request)
    
    messages.success(request,("You have been logged out!!!!!!"))
    return redirect('welcome')




def register_user(request):
    
   if request.method == "POST":
        username =request.POST.get("username")
        fname= request.POST.get("firstname")
        lname = request.POST.get("lastname")
        email= request.POST.get("email")
        password1= request.POST.get("password1")
        password2= request.POST.get("password2")
        if password1 == password2 :
            if User.objects.filter(username =username).exists():
                messages.error(request,("Whoops,there was a problem regsitering pls try again......"))
               
                return redirect('register')
            else:
                user =User.objects.create_user(username =username,email=email ,password=password1,first_name =fname, last_name=lname)
                login(request,user)
                messages.success(request,("You Have Regsitered Successfully Welcome......"))
                name =request.user
                
                return redirect('login')

   else:
        return render(request,'register.html',{
            
        }) 
   























#Admin
#hussein
#yinkus
#lawalhussein775@gmail.com


