# Generated by Django 3.2.2 on 2021-10-03 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(blank=True, default=None, null=True)),
                ('date_seen', models.DateTimeField(blank=True, default=None, null=True)),
                ('type', models.IntegerField(choices=[(0, 'Reservation'), (1, 'Payment'), (2, 'Service'), (3, 'Comment'), (4, 'User')])),
                ('link', models.URLField(blank=True, default=None, max_length=400, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
