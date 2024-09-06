# Generated by Django 4.2.6 on 2024-08-08 08:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0041_dukalako_likes_dukalako_profile_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dukalako',
            name='PichaYaPost',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Picha Ya Post'),
        ),
        migrations.AddField(
            model_name='dukalako',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_dukalako', to=settings.AUTH_USER_MODEL),
        ),
    ]
