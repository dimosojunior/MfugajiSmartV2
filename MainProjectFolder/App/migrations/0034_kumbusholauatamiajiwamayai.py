# Generated by Django 4.2.6 on 2024-08-03 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0033_ainazachanjo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KumbushoLaUatamiajiWaMayai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KiasiChaMayai', models.IntegerField(verbose_name='Kiasi Cha Mayai')),
                ('SikuYaNgapiTokaKuatamiwa', models.IntegerField(verbose_name='Siku Ya Ngapi Tangu Kuatamiwa')),
                ('JinaLaUlipoYatoaMayai', models.CharField(blank=True, max_length=200, null=True, verbose_name='Jina La UlipoYatoa Mayai au Alama')),
                ('NambaYakeYaSimu', models.CharField(blank=True, max_length=13, null=True, verbose_name='Namba yake Ya Simu')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, verbose_name='Namba Yako ya Simu')),
                ('username', models.CharField(blank=True, max_length=13, null=True, verbose_name='Jina Lako Kamili')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email Yako')),
                ('Location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Mahali')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('AinaYaKuku', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.ainazakuku', verbose_name='Aina Ya Kuku')),
            ],
            options={
                'verbose_name_plural': 'Kumbusho La Uatamiaji Wa Mayai',
            },
        ),
    ]
