from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Interventions

class InterventionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interventions
        fields = ('id', 'libelle', 'description', 'intervenant', 'lieu', 'date', 'statut')
