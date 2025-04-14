from .models import Reservation
from django import forms
import datetime
from django.core.exceptions import ValidationError


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('name', 'seats', 'date', 'time')
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'}
            ),
            'seats': forms.NumberInput(
                attrs={'min': 1, 'max': 6}
            )
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < datetime.date.today():
            raise ValidationError('the date cannot be in the past')
        if date.weekday() == 6:  # Sunday is 6
            raise ValidationError('Sorry we are close on Sundays '
                                  'Please choose another day')
        return date
