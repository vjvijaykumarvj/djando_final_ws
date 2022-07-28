from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def Register(request):
    if request.method =='GET':
        return render(request,'register_app/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        #firstname = request.POST['firstname']
        #lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        #validation process start here
        if username== '' or email == '' or password =='' or cpassword == '':
            messages.error(request,'mandatary fields are missing *')
            return render(request,'register_app/register.html')
        # password and conform password not matched give the error
        if password != cpassword:
            messages.error(request, 'Password cpassword not matched')
            return render(request, 'register_app/register.html')
        # user already exists give the error messege
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'register_app/register.html')
        # email already exists give the error messege
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists')
            return render(request,'register_app/register.html')
        #if there is no error go for the login page
        else:
            User.objects.create_user(username=username,email=email,password=password,cpassword=cpassword)
            return redirect('/register/login/')
def Login(request):
    if request.method== 'GET':
        return render(request,'register_app/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #validation start here
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home/')
            # return redirect('/register/profile/home/')
        else:
            messages.error(request,'Username/password incorrect')
            return redirect('/register/login/')
def LogOut(request):
    logout(request)
    return redirect('/register/login/')
def Profile(request):
    return render(request,'register_app/profile.html')
