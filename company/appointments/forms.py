from django import forms
from .models import Appointments

class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Appointments
        fields = ('__all__')
    