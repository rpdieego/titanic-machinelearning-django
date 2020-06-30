from django import forms
from .models import PassengerDB

class PassengerForm(forms.ModelForm):
    class Meta:
        model = PassengerDB
        fields = ['passenger_name','passenger_age','completed']