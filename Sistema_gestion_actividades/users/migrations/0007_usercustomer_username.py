# Generated by Django 4.1 on 2023-08-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_usercustomer_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercustomer',
            name='username',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]