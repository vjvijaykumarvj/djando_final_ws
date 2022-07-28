from django import forms
from.models import Rooms

class Room_form(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'
