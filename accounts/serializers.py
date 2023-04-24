from rest_framework import serializers
from accounts.models import Patient,Doctor


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ()


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ()

