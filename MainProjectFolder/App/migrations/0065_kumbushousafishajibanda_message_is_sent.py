# Generated by Django 4.2.6 on 2024-08-30 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0064_kumbushousafishajibanda_day_is_reached'),
    ]

    operations = [
        migrations.AddField(
            model_name='kumbushousafishajibanda',
            name='message_is_sent',
            field=models.BooleanField(default=False),
        ),
    ]
