# Generated by Django 4.2.6 on 2023-10-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_technology_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='photo',
            field=models.ImageField(upload_to='portfolio/technologies'),
        ),
    ]
