from django.shortcuts import render,redirect
from .models import  Employee_model
from .forms import Employee_Form
# Create your views here.
def VIJAY(request):
    if request.method == 'GET':
        emp_db = Employee_Form
        emp_dict={
            'employee' : emp_db
        }
        return render(request,'VIJAY_app/vijay.html',context=emp_dict)
    elif request.method=='POST':
        employee = Employee_Form(request.POST)
        if employee.is_valid():
            eno = employee.cleaned_data['eno']
            name = employee.cleaned_data['name']
            age = employee.cleaned_data['age']
            salary = employee.cleaned_data['salary']
            address = employee.cleaned_data['address']
            employee= employee


