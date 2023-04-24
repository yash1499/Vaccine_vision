from django.shortcuts import render
from rest_framework import viewsets
from vaccination.models import VaccinationChart
from vaccination.serializers import VaccinationSerializer
# Create your views here.


class DoctorView(viewsets.ModelViewSet):

    serializer_class = VaccinationSerializer
    model = VaccinationChart

    def get_queryset(self):
        data = self.model.objects.all()
        return data

class PatientView(viewsets.ModelViewSet):

    serializer_class = VaccinationSerializer
    model = VaccinationChart

    def get_queryset(self):
        data = self.model.objects.all()
        return data