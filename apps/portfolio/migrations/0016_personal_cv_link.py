# Generated by Django 4.2.6 on 2023-11-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_portfolio_object_fit'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='cv_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]