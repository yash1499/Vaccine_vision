from rest_framework import serializers
from vaccination.models import VaccinationChart
from accounts.models import Doctor,Patient


class DoctorField(serializers.RelatedField):

    queryset = Doctor.objects.all()

    def to_internal_value(self, data):
        return self.queryset.get(id=data)

    def to_representation(self, value):
        return {'id': value.id,
                'email': value.email
                }

class PatientField(serializers.RelatedField):

    queryset = Patient.objects.all()

    def to_internal_value(self, data):
        return self.queryset.get(id=data)

    def to_representation(self, value):
        return {'id': value.id,
                'email': value.email
                }

class VaccinationSerializer(serializers.ModelSerializer):
    patient=PatientField()
    doctor=DoctorField()

    class Meta:
        model = VaccinationChart
        fields = ('id','patient','doctor','name', 'date_of_vaccination',)