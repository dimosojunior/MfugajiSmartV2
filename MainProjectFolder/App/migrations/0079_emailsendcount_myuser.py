# Generated by Django 4.2.6 on 2024-09-11 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0078_emailsendcount_dukalako_approvedmaelezopost_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSendCount_MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('phone', models.CharField(blank=True, max_length=13, null=True, verbose_name='Namba Yako ya Simu')),
                ('username', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina Lako Kamili')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email Yako')),
                ('Location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Mahali')),
                ('ApprovedUser', models.CharField(blank=True, max_length=500, null=True, verbose_name='Posti Aliyohakiki')),
                ('ApprovedMaelezoUser', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Maelezo Ya Posti Aliyohakiki')),
                ('last_sent', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Email Count Users',
            },
        ),
    ]
