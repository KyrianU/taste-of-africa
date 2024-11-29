from .models import Reservation
from django import forms
from django.conf import settings
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
        }


class EditReservations(forms.ModelForm):

    # compare user input agaisnt current date ans throws an error
    # if data happens to be in the past

    def clean_date(self):
        date = self.cleaned_data('date')
        if date < datetime.date.now():
            raise forms.ValidationError('the date cannot be in the past')
        return data

        class Meta:
            model = Resevation
            fields = ('name', 'seats', 'date', 'time')
            widgets = {
                'date': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control',
                           'placeholder': 'Select a date',
                           'type': 'date'}
                ),
            }
