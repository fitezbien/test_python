# Generated by Django 3.0.4 on 2020-03-09 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200309_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interventions',
            name='date_intervention',
            field=models.DateField(default=datetime.datetime(2020, 3, 9, 19, 22, 50, 328589)),
        ),
    ]
