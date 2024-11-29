from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Menu(models.Model):
    """
    Menu items model
    """

    MENU_ITEMS = (
        ('Starters', 'starters'),
        ('Mains', 'mains'),
        ('Desserts', 'desserts'),
    )

    item = models.CharField(max_length=25, choices=MENU_ITEMS)
    name = models.CharField(max_length=50)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return str(self.name)

