# Generated by Django 3.2.2 on 2021-09-28 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_serviceconsumed_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceconsumed',
            name='date_created',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
