# Generated by Django 3.2.2 on 2021-09-27 11:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import reservation.models.payment
import reservation.models.reservation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('residence', '0001_initial'),
        ('common', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_number', models.CharField(max_length=10, unique=True)),
                ('date_from', models.DateField(default=None, verbose_name='date_from')),
                ('date_until', models.DateField(default=None, verbose_name='date_until')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Cancelled'), (2, 'Pending'), (3, 'Active')], default=2)),
                ('date_cancelled', models.DateTimeField(blank=True, default=None, null=True)),
                ('date_finalized', models.DateTimeField(blank=True, default=None, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_created')),
                ('observations', models.CharField(default=None, max_length=200, null=True)),
                ('reject_reason', models.CharField(blank=True, default=None, max_length=400, null=True)),
                ('contract', models.FileField(blank=True, default=None, null=True, upload_to='media/contracts')),
                ('bed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='residence.bed')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceConsumed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(blank=True, default=None)),
                ('amount', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('payment_date', models.DateField(default=None, null=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.reservation')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_consumed', to='residence.serviceoffered')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='service',
            field=models.ManyToManyField(related_name='serviceconsumed', through='reservation.ServiceConsumed', to='residence.ServiceOffered'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Cancelled'), (2, 'Pending'), (3, 'Active')], default=2)),
                ('amount', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('year_month', models.IntegerField(validators=[reservation.models.payment.year_month_validate])),
                ('payment_date', models.DateField()),
                ('observations', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('reject_reason', models.CharField(blank=True, default=None, max_length=400, null=True)),
                ('date_status', models.DateField(blank=True, default=None, null=True)),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='media/payments')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.paymentmethod')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('review', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('date_created', models.DateTimeField(blank=True, default=None, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Cancelled'), (2, 'Pending'), (3, 'Active')], default=2)),
                ('reject_reason', models.CharField(default=None, max_length=400, null=True)),
                ('date_rejected', models.DateTimeField(default=None, null=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.reservation')),
            ],
        ),
    ]
