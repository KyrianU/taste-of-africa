from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

from django.db.models import IntegerField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.


time_slots = (
    ("12:30", "12:30"),
    ("13:30", "13:30"),
    ("14:30", "14:30"),
    ("15:30", "15:30"),
    ("16:30", "16:30"),
    ("17:30", "17:30"),
    ("18:30", "18:30"),
    ("19:30", "19:30"),
    ("20:30", "20:30"),
    ("21:30", "21:30"),

)


class Reservation(models.Model):
    """
    Model representing a reservation system in the restaurant.
    """

    def validate_date(date):
        if date < datetime.date.today():
            raise ValidationError("The date cannot be in the past")
        return date

    seats = models.IntegerField(
        null=False,
        blank=False,
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6),
        ]
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20, null=True)
    date = models.DateField(
        null=True, blank=True, default=None, validators=[validate_date])
    time = models.CharField(
        max_length=20, choices=time_slots, default="12:30")
    date_booked = models.DateField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return str(self.id)
