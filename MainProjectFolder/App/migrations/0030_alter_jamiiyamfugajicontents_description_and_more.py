# Generated by Django 4.2.6 on 2024-07-31 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0029_ainazakuku_finisherfeed_ainazakuku_growerfeed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jamiiyamfugajicontents',
            name='Description',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='maktabayalishecontents',
            name='Description',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='matumizisahihiyaindibata',
            name='Description',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='muongozowalishe',
            name='Description',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='Maelezo',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
