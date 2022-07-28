from django.shortcuts import render
from .models import Student,Contact
# Create your views here.
from django.contrib import messages

def student_registration(request):
    if request . method == 'GET':
        return render(request,'reg_app/student_registration.html')

    elif request . method =='POST':
        First_name = request . POST . get('firstname')
        Last_name = request . POST . get('lastname')
        Gender = request . POST . get('gender')
        Contact_number = request . POST . get('contactnumber')
        Emailid = request . POST . get('emailid')
        Address = request . POST . get('address')
        City = request . POST . get('city')
        State= request . POST . get('state')
        Python = request.POST.get('python')
        Django = request.POST.get('Django')
        Java = request.POST.get('Java')
        Bigdata = request.POST.get('Bigdata')
        User_name = request . POST . get('username')
        Password = request . POST . get('password')
        Confome_password = request.POST.get('confomepassword')



        #Creat the student MODEL:
        student=Student(firstname=First_name,lastname=Last_name,gender=Gender,contactNumber=Contact_number,
                        emailId=Emailid,address=Address,city=City,state=State,python=Python,django=Django,
                        java=Java,username=User_name,password=Password,confomepassword=Confome_password)
        student.save()
        #with above data create a student record DB

        #send the response to CLIENT:
        student_dict={
            'firstname' : First_name,
            'lastname' :  Last_name,
            'gender' : Gender,
            'contactnumber' : Contact_number,
            'emailid' : Emailid,
            'address' : Address,
            'city' : City,
            'state' : State,
            'python': Python,
            'Django': Django,
            'Java': Java,
            'Bigdata': Bigdata,
            'username' : User_name,
            'password' : Password,
            'confomepassword' : Confome_password

        }

        return render(request,'reg_app/student_details.html',context=student_dict)


def Contactus(request):
    if request.method== 'GET':
        return render(request,'reg_app/contact.html')
    else:
        username = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        user = Contact(name = username,email=email,message=message)
        user.save()
        messages.success(request, 'Succesfully contactus')
        return render(request,'reg_app/contact.html')



