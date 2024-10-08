# Generated by Django 4.2.6 on 2024-07-23 11:59

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_taarifazakuku_total_food_price_wiki_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdadiYaKuku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdadiYaKuku', models.IntegerField(verbose_name='IdadiYaKuku')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Idadi Ya Kuku',
            },
        ),
        migrations.CreateModel(
            name='JamiiYaMfugajiCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=500, verbose_name='Category')),
                ('Picha', models.ImageField(blank=True, null=True, upload_to='media/PichaZaVirutubisho/', verbose_name='Picha')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Makundi Ya Jamii Ya Mfugaji',
            },
        ),
        migrations.CreateModel(
            name='MaktabaYaLisheCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=500, verbose_name='Category')),
                ('Picha', models.ImageField(blank=True, null=True, upload_to='media/PichaZaVirutubisho/', verbose_name='Picha')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Makundi Ya Maktaba Ya Lishe',
            },
        ),
        migrations.CreateModel(
            name='MatumiziSahihiYaIndibata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=5000, verbose_name='Title')),
                ('Picha', models.ImageField(blank=True, null=True, upload_to='media/PichaZaVirutubisho/', verbose_name='Picha')),
                ('Description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/MaktabaYaLishePDF')),
                ('Prepared_By', models.CharField(blank=True, max_length=500, null=True, verbose_name='Imeandaliwa Na:')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Matumizi Sahihi Ya Indibata',
            },
        ),
        migrations.CreateModel(
            name='MuongozoWaLishe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=5000, verbose_name='Title')),
                ('Picha', models.ImageField(blank=True, null=True, upload_to='media/PichaZaVirutubisho/', verbose_name='Picha')),
                ('Description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/MaktabaYaLishePDF')),
                ('Prepared_By', models.CharField(blank=True, max_length=500, null=True, verbose_name='Imeandaliwa Na:')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Muongozo Wa Lishe',
            },
        ),
        migrations.AddField(
            model_name='ainazakuku',
            name='PichaYaKuku',
            field=models.ImageField(blank=True, null=True, upload_to='media/PichaZaKuku/', verbose_name='Picha Ya Kuku'),
        ),
        migrations.CreateModel(
            name='MaktabaYaLisheContents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=5000, verbose_name='Title')),
                ('Picha', models.ImageField(blank=True, null=True, upload_to='media/PichaZaVirutubisho/', verbose_name='Picha')),
                ('Description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/MaktabaYaLishePDF')),
                ('Prepared_By', models.CharField(blank=True, max_length=500, null=True, verbose_name='Imeandaliwa Na:')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('CategoryName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.maktabayalishecategories', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Ndani Ya Makundi Maktaba Ya Lishe',
            },
        ),
        migrations.CreateModel(
            name='JamiiYaMfugajiContents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=100, verbose_name='Jina Kamili')),
                ('Location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Mahali')),
                ('Title', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Title')),
                ('Picha', models.ImageField(blank=True, null=True, upload_to='media/PichaZaVirutubisho/', verbose_name='Picha')),
                ('Description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/MaktabaYaLishePDF')),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Phone', models.CharField(blank=True, default='+255', max_length=13, null=True)),
                ('Youtube', models.CharField(blank=True, max_length=1000, null=True)),
                ('WhatsappLink', models.CharField(blank=True, max_length=1000, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('CategoryName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.jamiiyamfugajicategories', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Ndani Ya Jamii Ya Mfugaji',
            },
        ),
    ]
