# Generated by Django 3.0.7 on 2020-07-30 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_factory', '0008_auto_20200716_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrymodel',
            name='contractDate',
            field=models.DateField(default=datetime.datetime(2020, 7, 30, 16, 29, 18, 797299)),
        ),
        migrations.AlterField(
            model_name='entrymodel',
            name='cost',
            field=models.CharField(default='50000.00', max_length=100),
        ),
    ]
