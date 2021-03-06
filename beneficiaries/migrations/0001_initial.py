# Generated by Django 4.0.3 on 2022-03-07 14:27

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
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('profile_picture', models.ImageField(upload_to='beneficiaries/profile_pictures/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('donation_type', models.CharField(max_length=100)),
                ('delivered', models.BooleanField(default=False)),
                ('delivered_date', models.DateTimeField(blank=True, null=True)),
                ('delivery_faiiled', models.BooleanField(default=False)),
                ('delivery_failed_reason', models.CharField(max_length=100)),
                ('dropoff_address', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beneficiaries.beneficiary')),
            ],
        ),
        migrations.CreateModel(
            name='PickupStations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('building', models.CharField(max_length=100)),
                ('doations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beneficiaries.donations')),
            ],
        ),
    ]
