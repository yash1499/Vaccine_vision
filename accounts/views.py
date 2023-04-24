from django.shortcuts import HttpResponse,render
from django.views.generic import TemplateView
from vaccination.models import VaccinationChart,ZipcodeToLatLog
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from accounts.models import *
from django.contrib.auth.base_user import AbstractBaseUser

factory = APIRequestFactory()

def home(request):
	return render(request, 'accounts/home.html')

def search_vaccine(search_by,value):
    if search_by == 'Search By child Patient':
        return VaccinationChart.objects.filter(patient__first_name__contains=value)
    elif search_by == 'Search By Pincode':
        return VaccinationChart.objects.filter(patient__pincode__contains=value)
    if search_by == 'Search By Doctor':
        return VaccinationChart.objects.filter(doctor__first_name__contains=value)
    if search_by == 'Search By Year':
        return VaccinationChart.objects.filter(date_of_vaccination__year__contains=value)

def search(request):
    if request.GET.get('s',False) and request.GET.get('q',False):
        vaccination_objects = search_vaccine(request.GET.get('s',False),request.GET.get('q',False))
    else:
        vaccination_objects = VaccinationChart.objects.all()

    if len(vaccination_objects) > 100:
        vaccination_objects = vaccination_objects
    context = {
        'vaccines': vaccination_objects,
    }
    template = loader.get_template('accounts/search_vaccine.html')
    return HttpResponse(template.render(context,request))

def home1(request):
	return render(request,'accounts/form.html')

def results(request):
	return render(request,'accounts/search_by_child_id.html')


def results1(request):
    q = request.GET.get('q', None)
    if q:
        Patient_name=VaccinationChart.objects.filter(Patient_id=q)
        return render(request,'accounts/search_by_child_id.html', {'Patient_name': Patient_name})
    else:
        return HttpResponse('Please enter a valid input.')

def results2(request):
	return render(request,'accounts/search_by_doctor_id.html')



def results3(request):
    q = request.GET.get('q', None)
    if q:
        Patient_name=VaccinationChart.objects.filter(Doctor_personal_id=q)
        return render(request,'accounts/search_by_doctor_id.html', {'Patient_name': Patient_name})
    else:
        return HttpResponse('Please enter a valid input.')

def results4(request):
	return render(request,'accounts/search_by_pincode.html')

def results5(request):
    q = request.GET.get('q', None)
    if q:
        Patient_name=VaccinationChart.objects.filter(Pincode=q)
        return render(request,'accounts/search_by_pincode.html', {'Patient_name': Patient_name})
    else:
        return HttpResponse('Please enter a valid input.')	


def results6(request):
	return render(request,'accounts/search_by_year.html')

def results7(request):
    q = request.GET.get('q', None)
    if q:
        Patient_name=VaccinationChart.objects.filter(Date_of_vaccination__year=q)
        return render(request,'accounts/search_by_year.html', {'Patient_name': Patient_name})
    else:
        return HttpResponse('Please enter a valid input.')
import json

def results8(request):
    vaccination_objects = VaccinationChart.objects.all()[0:300]
    data = []
    zipcodes = {}
    for vacc in vaccination_objects:
        pzip = vacc.patient.pincode
        if zipcodes.get(pzip,False):
            zipcodes[pzip][2] += 1
        else:
            z = ZipcodeToLatLog.objects.filter(zipcode = pzip)
            if z:
                z = z[0]
                zipcodes[pzip] =[z.lat,z.log,1]

    for key,val in zipcodes.items():
        data.append(val)

    return render(request,'accounts/heatmap.html',{'data':json.dumps(data)})


from tablib import Dataset
from accounts.admin import PatientResource

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PatientResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')



