from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def Login(request):
    if request.method=='GET':
       return render(request,'login_registration_app/sign_form.html')
    elif request.method=='POST':
        # 1 read the all input Data From the request:::
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        # 2. Validate input Data
        # 2.1. Check for mandatory fields
        if username=='' or email=='' or password=='' or  cpassword=='':
            messages.error(request,'mandatary fields are missing !!!')
            return render(request,'login_registration_app/sign_form.html')
        # 2.2. Check for password & confirm password whether both are same or not
        if password != cpassword:
            messages.error(request,'Password, Confirm passwords are not maching !!!')
            return render(request,'login_registration_app/sign_form.html')
        # 2.3. If user is already exist then give error message
        if User.objects.filter(username=username).exists():
            messages.error(request,'User name is already exists')
            return render(request,'login_registration_app/sign_form.html')

        #2.4 if emailid is already exist then give error message:
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already exixts')
            return render(request,'login_registration_app/sign_form.html')
        else:
            # if no validation error then save to data in DB:
             User.objects.create_user(username=username,first_name=first_name,last_name=last_name,
                                      email=email,password=password)
            #after saving its redirect to LOGIN Page:
             messages.info(request, "Account Created Successfully, Please login to continue")
             return redirect('/registersign/user_login/')

def User_login(request):
    if request.method=='GET':
        return render(request,'login_registration_app/user_login.html')
    elif request.method=='POST':
        #perforem the userid and password validations:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)#user=None

        if User is not None:
            #allow to user login:::
            login(request,user)
            return redirect('/registersign/userprofile/')
        else:
            messages.error(request,'Username/Password are Incorrect !!!')
            return redirect('/registersign/user_login/')

def userprofile(request):
    return render(request,'login_registration_app/userprofile.html')

def user_logout(request):
    logout(request)
    return redirect('/registersign/user_login/')
