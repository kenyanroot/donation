# Generated by Django 4.0.1 on 2022-04-18 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0012_alter_ngodonations_delivery_failed_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngodonations',
            name='beneficiary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NGO.ngoprofile'),
        ),
    ]
