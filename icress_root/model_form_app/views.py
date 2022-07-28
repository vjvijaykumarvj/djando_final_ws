from django.shortcuts import render,redirect
from.models import Employee_form
from .forms import Employee_Forms
# Create your views here.

def Model_Form(request):
    if request.method == 'GET':
        emp_forms=Employee_Forms()
        emp_list=Employee_form.objects.all()
        emp_dict={
           'emp_forms' : emp_forms,
           'emp_list' : emp_list
        }
        return render(request,'model_form_app/model_form.html',context=emp_dict)

    elif request.method=='POST':
        emp_forms=Employee_Forms(request.POST)
        if emp_forms.is_valid():
            emp_forms.save()
            return redirect('/modelformcreate/model_form/')


def Emp_Update(request,pk):
    if request.method=='GET':
        employee=Employee_form.objects.get(id=pk)
        emp_forms = Employee_Forms(instance=employee)
        emp_list=Employee_form.objects.all()
        emp_dict={
            'emp_forms' : emp_forms,
            'emp_list' : emp_list
        }
        return render(request,'model_form_app/model_form.html',context=emp_dict)
    elif request.method=='POST':
        emp_list = Employee_form.objects.get(id=pk)
        emp_forms = Employee_Forms(request.POST,instance=emp_list)
        if emp_forms.is_valid():
            emp_forms.save()
            return redirect('/modelformcreate/model_form/')

def Emp_Delete(request,pk):
    emp_list=Employee_form.objects.get(id=pk)
    emp_list.delete()
    return redirect('/modelformcreate/model_form/')












'''    elif request.method == 'POST':
        emp_forms=Employee_Forms(request.POST)
        if emp_forms.is_valid():
            eno=emp_forms.cleaned_data['eno']
            name=emp_forms.cleaned_data['name']
            age=emp_forms.cleaned_data['age']
            salary=emp_forms.cleaned_data['salary']
            address=emp_forms.cleaned_data['address']
            employee = Employee_form(eno=eno,name=name,age=age,salary=salary,address=address)
            employee.save()
            return redirect('/modelformcreate/model_form/')
'''
    # option :1
    # elif request.method == 'POST':
    #     eno=request.POST.get('eno')
    #     name=request.POST.get('name')
    #     age=request.POST.get('age')
    #     salary=request.POST.get('salary')
    #     address=request.POST.get('address')
    #     employee=Employee_form(eno=eno,name=name,age=age,salary=salary,address=address)
    #     employee.save()
    #     return redirect('/modelformcreate/model_form/')