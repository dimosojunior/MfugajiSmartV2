# Generated by Django 4.2.6 on 2024-08-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0060_alter_notification_duka_lako'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Picha Ya Aliye Like'),
        ),
        migrations.AddField(
            model_name='notification',
            name='PostOwner',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Mmiliki Wa Posti: '),
        ),
    ]
