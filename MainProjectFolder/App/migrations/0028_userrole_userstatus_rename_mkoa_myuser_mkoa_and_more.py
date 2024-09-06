# Generated by Django 4.2.6 on 2024-07-31 03:22

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0027_levelzawafugaji_myuser_ainayakuku_mikoa_myuser_level_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.CharField(max_length=100, verbose_name='Aina Ya User')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'User Role',
            },
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=100, verbose_name='Status')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Status Za Wafugaji',
            },
        ),
        migrations.RenameField(
            model_name='myuser',
            old_name='MKoa',
            new_name='Mkoa',
        ),
        migrations.RemoveField(
            model_name='mikoa',
            name='Chakula',
        ),
        migrations.RemoveField(
            model_name='mikoa',
            name='price',
        ),
        migrations.AddField(
            model_name='myuser',
            name='LevelImage',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Picha Ya Nyota'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='Maelezo',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Picha Ya Mtu'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='Role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.userrole', verbose_name='Aina Ya User'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='Status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.userstatus', verbose_name='Status Ya Mfugaji'),
        ),
    ]
