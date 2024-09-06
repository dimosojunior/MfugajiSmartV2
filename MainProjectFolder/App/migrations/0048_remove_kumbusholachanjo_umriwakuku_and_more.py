# Generated by Django 4.2.6 on 2024-08-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0047_idadiyakilos_alter_idadiyakuku_idadiyakuku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kumbusholachanjo',
            name='UmriWaKuku',
        ),
        migrations.RemoveField(
            model_name='vyakula',
            name='TotalPercentageRequired',
        ),
        migrations.AddField(
            model_name='vyakula',
            name='TotalPercentageRequired_Finisher',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Finisher - %'),
        ),
        migrations.AddField(
            model_name='vyakula',
            name='TotalPercentageRequired_Grower',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Grower - %'),
        ),
        migrations.AddField(
            model_name='vyakula',
            name='TotalPercentageRequired_Layer',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Layer - %'),
        ),
        migrations.AddField(
            model_name='vyakula',
            name='TotalPercentageRequired_Starter',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Starter - %'),
        ),
    ]
