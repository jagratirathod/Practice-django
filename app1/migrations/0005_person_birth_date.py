# Generated by Django 4.1.4 on 2023-04-24 13:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
