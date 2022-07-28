from django . shortcuts import render
from datetime import datetime


def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contactus.html')

def about_us(request):
    return render(request,'aboutus.html')

def login_logout(request):
    return render(request,'login_logout.html')

def employee_registration(request):
    if request . method == 'GET':
        return render(request,'employee.html')
    elif request . method == 'POST':
        fname=request . POST .get('first_name')
        lname=request . POST .get('last_name')
        age=request . POST .get('age')
        contact_number=request .POST . get('Contact Number')
        address=request . POST .get('address')


        namedict={
             'first_name':fname,
             'last_name':lname,
             'age':age,
             'Contact Number':contact_number,
             'address':address,
        }
        return render(request,'employee_details.html',context=namedict)

class Employee:
    def __init__(self,name,age,address,salary):
        self.name=name
        self.age=age
        self.address=address
        self.salary=salary
emp_vijay = Employee('vijay', 25, 'Banglore', 35000)
emp_hari=Employee('hari',25,'venkatagiri',35000)

def dtl(request):
    msg='hello welcome to vijaykumar this is your details'
    name='vijaykumar'
    age=24
    list=['apple','bananna','anasa','mango']
    marriage_status=False
    Employee = emp_vijay
    Employee = emp_hari
    emp_list=[emp_vijay,emp_hari]
    Today_date=datetime.now()

    topics={
        1001:'python',
        1002:'java',
        1003:'Django'
    }

    data={
        'msg_key' : msg,
        'name_key' : name,
        'age_key' : age,
        'list_key' : list,
        'topic_key' : topics,
        'Marriage_status' : marriage_status,
        'Employee_details' : Employee,
        'emp_list'  :  emp_list,
        'today_date' : Today_date

        }
    return render(request,'dtl.html',context=data)
