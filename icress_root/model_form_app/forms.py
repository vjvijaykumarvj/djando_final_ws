from django import forms
from .models import Employee_form

class Employee_Forms(forms.ModelForm):
    class Meta:
        model = Employee_form
        fields='__all__'
        widgets={
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'eno' : forms.TextInput(attrs={'class' : 'form-control'}),
            'age' : forms.TextInput(attrs={'class' : 'form-control'}),
            'salary' : forms.TextInput(attrs={'class' : 'form-control'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control'}),
        }
