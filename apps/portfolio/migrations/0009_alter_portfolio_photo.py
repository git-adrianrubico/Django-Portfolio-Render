# Generated by Django 4.2.6 on 2023-11-11 07:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_portfolio_link3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]