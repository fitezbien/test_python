from django.db import models
from datetime import datetime

class Interventions(models.Model):
    libelle = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True)
    intervenant = models.CharField(max_length=256, blank=True)
    lieu = models.CharField(max_length=256, blank=True)
    date = models.DateField(default=datetime.today(), blank=True)
    statut = models.CharField(max_length=256, blank=True)
