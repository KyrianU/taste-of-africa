# Generated by Django 5.1 on 2024-10-15 01:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='image',
        ),
        migrations.AddField(
            model_name='menu',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
