# Generated by Django 4.2.6 on 2024-08-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0045_remove_vyakula_calc_remove_vyakula_carbo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vyakulaorder',
            name='TotalFoodMixerPercentage',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumla Ya Percentage Ya Vyakula Vyote - %'),
        ),
    ]
