# Generated by Django 4.2.1 on 2023-06-12 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
