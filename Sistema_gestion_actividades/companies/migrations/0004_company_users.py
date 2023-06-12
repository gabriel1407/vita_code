# Generated by Django 4.2.1 on 2023-06-12 22:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0003_company_is_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
