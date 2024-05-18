# Generated by Django 4.2.10 on 2024-05-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produce', '0005_order_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderservices',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата оказания услуг'),
        ),
        migrations.AlterField(
            model_name='orderservices',
            name='services',
            field=models.ManyToManyField(blank=True, null=True, related_name='services', to='produce.services', verbose_name='Услуги'),
        ),
        migrations.AlterField(
            model_name='orderservices',
            name='time_end',
            field=models.TimeField(auto_now_add=True, null=True, verbose_name='Удобное время оказания услуг по'),
        ),
        migrations.AlterField(
            model_name='orderservices',
            name='time_start',
            field=models.TimeField(auto_now_add=True, null=True, verbose_name='Удобное время оказания услуг с'),
        ),
    ]