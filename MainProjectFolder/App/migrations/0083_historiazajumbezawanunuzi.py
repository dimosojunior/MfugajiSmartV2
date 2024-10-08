# Generated by Django 4.2.6 on 2024-09-11 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0082_wanunuzi_message_emailsendcount_wanunuzi'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaZaJumbeZaWanunuzi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JinaLaMnunuzi', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina La Mnunuzi')),
                ('NambaYaSimuYaMnunuzi', models.CharField(blank=True, max_length=13, null=True, verbose_name='Namba Ya Simu Ya Mnunuzi')),
                ('Mkoa', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mkoa')),
                ('Wilaya', models.CharField(blank=True, max_length=500, null=True, verbose_name='Wilaya')),
                ('last_sent', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Historia Za Jumbe Za Wanunuzi',
            },
        ),
    ]
