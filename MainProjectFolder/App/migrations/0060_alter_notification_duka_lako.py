# Generated by Django 4.2.6 on 2024-08-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0059_remove_notification_user_notification_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='duka_lako',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Post Aliyo Like: '),
        ),
    ]
