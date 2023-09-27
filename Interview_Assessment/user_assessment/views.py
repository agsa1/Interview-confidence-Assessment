from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user = authenticate(request,username=u, password=p)
        if user is not None:
            login(request,user)
            return redirect("user_assessment:home")
    return render(request,'login.html')

def signup(request):
    if (request.method=="POST"):
        u = request.POST["u"]
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST["cp"]
        if cp == p:
            user = User.objects.create_user(username=u,email=e,password=p)
            user.save()
            return redirect('user_assessment:login_view')
        else:
            messages.error(request,"Passwords are not same")

    return render(request,'signup.html')

def home(request):
    return render (request,"home.html")

def user_logout(request):
    logout(request)
    return redirect('user_assessment:login_view')