from django.shortcuts import render
from .forms import StudentDJF
from .models import StudentDjangoForms
# Create your views here.

def Load_Student_djforms(request):
    if request.method == 'GET':
         Student_djforms=StudentDJF()
         dict={
            'student_form'  :  Student_djforms
         }
         return render(request, 'student_form_app/student_forms.html', context=dict)
    elif request.method=='POST':
        Student_djforms = StudentDJF(request.POST)
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        gender=request.POST.get('Gender')
        contactnumber=request.POST.get('ContactNumber')
        emailid=request.POST.get('Emailid')
        address=request.POST.get('Address')
        confirm_Emailid=request.POST.get('Confirm_Emailid')
        date_of_Birth=request.POST.get('Date_of_Birth')
        city=request.POST.get('City')
        state=request.POST.get('State')
        python=request.POST.get('Python')
        Java=request.POST.get('Java')

        studentRDF=StudentDjangoForms(firstname=firstname,lastname=lastname,Gender=gender,ContactNumber=contactnumber,
                                      Emailid=emailid,Address=address,Confirm_Emailid=confirm_Emailid,Date_of_Birth=date_of_Birth,
                                      City=city,State=state,Python=python,Java=Java)
        studentRDF.save()

        dict={
            'Student_djforms' : Student_djforms,
            'firstname' : firstname,
            'lastname'  :  lastname,
            'gender'   :  gender,
            'contactnumber'   :  contactnumber,
            'emailid'   :  emailid,
            'address'   :  address,
            'confirm_Emailid'   :  confirm_Emailid,
            'DOB'   :  date_of_Birth,
            'City'   :  city,
            'State'   :  state,
            'Python'   :  python,
            'Java'   :  Java,
           'isFormSumbmitte': 'yes'
        }
    return render(request,'student_form_app/student_forms.html',context=dict)
