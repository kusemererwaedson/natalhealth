# Generated by Django 5.1.3 on 2024-11-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_pregnancydetails_nin_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregnancydetails',
            name='nin_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
