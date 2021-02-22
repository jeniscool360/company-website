from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Appointment
        fields = ('__all__')
    