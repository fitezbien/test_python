# Generated by Django 3.0.4 on 2020-03-10 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200310_0827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interventions',
            old_name='nom_intervenant',
            new_name='intervenant',
        ),
        migrations.RemoveField(
            model_name='interventions',
            name='date_intervention',
        ),
        migrations.AddField(
            model_name='interventions',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 3, 10, 8, 39, 0, 698514)),
        ),
    ]