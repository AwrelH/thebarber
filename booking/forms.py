from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = [
            'name',
            'appointment_time',
            'appointment_type',
            'slots',
            'contact_info']
        widgets = {
            'appointment_time': DateInput()
        }
