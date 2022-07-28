from django import forms


class StudentDJF(forms.Form):
    firstname=forms.CharField(label='Enter First Name',
                              required=False,
                              widget=forms.TextInput(attrs={'placeholder' :  'Enter first name'}))
    lastname=forms.CharField(label='Enter Last Name',
                             required=False,
                             widget=forms.TextInput(attrs={'placeholder':  'Enter last name'}))
    gender_choose=(('male','Male'),('female','Female'))
    Gender=forms.ChoiceField(choices=gender_choose,widget=forms.RadioSelect,
                             label='select gender',
                             required=False)
    ContactNumber =forms.CharField()
    Emailid =forms.EmailField(label='Enter EmailId',
                              required=False)
    Confirm_Emailid=forms.EmailField(label='Confirm Emailid',
                                     required=False)
    Address =forms.CharField(label='Enter Address',
                             required=False,
                             widget=forms.Textarea)
    Date_of_Birth=forms.DateField(label='Enter your DOB',
                                  required=False,
                                  widget=forms.TextInput(attrs={'type' : 'date'}))
    choose_option=(('BGL','bangalore'),('ARVT','Amaravathi'),('HYD','Hydarabad'))
    City=forms.ChoiceField(label='Enter Your City',
                           required=False,
                           choices=choose_option)
    choose_option = (('KNTK', 'Karnataka'), ('AP', 'Andhrapradesh'), ('TS', 'Telangana'))
    State=forms.ChoiceField(label='Enter your State',
                            required=False,
                            choices=choose_option)
    Python=forms.BooleanField(label='Python',
                              required=False,)
    Java=forms.BooleanField(label='Java',
                            required=False)

