from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .mserializers import InterventionsSerializer
from .models import Interventions
from rest_framework.response import Response


class InterventionsViewSet(viewsets.ModelViewSet):
    queryset = Interventions.objects.all()
    serializer_class = InterventionsSerializer

    def list(self, request, *args, **kwargs):
        interventions = Interventions.objects.all()
        serializer = InterventionsSerializer(interventions, many=True)
        return Response(serializer.data)
