# Generated by Django 5.1.3 on 2024-11-17 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_nin_number_pregnancydetails_nin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregnancydetails',
            name='nin',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
