# Generated by Django 4.2.5 on 2023-12-23 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("model_inheritance", "0003_center_mycenter"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mycenter",
            options={"ordering": ["id"]},
        ),
    ]