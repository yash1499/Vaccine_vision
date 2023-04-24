from django.db import models

# Create your models here.


class VaccinationChart(models.Model):
    name = models.CharField(max_length=100)
    patient = models.ForeignKey('accounts.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('accounts.Doctor', on_delete=models.CASCADE)
    date_of_vaccination = models.DateField()

    class Meta:
        db_table = 'vaccination_chart'

class ZipcodeToLatLog(models.Model):
    zipcode = models.CharField(max_length=150,primary_key=True)
    lat = models.CharField(max_length=150)
    log = models.CharField(max_length=150)
    country = models.CharField(max_length=150,null=True)

    class Meta:
        db_table = 'zipcode'
