# Generated by Django 3.0.4 on 2020-03-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interventions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=256)),
                ('nom_intervenant', models.CharField(max_length=256)),
                ('lieu', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
