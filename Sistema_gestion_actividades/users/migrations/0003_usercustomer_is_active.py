# Generated by Django 4.2.1 on 2023-07-31 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usercustomer_email_usercustomer_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercustomer',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]