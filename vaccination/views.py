from django.shortcuts import render
from rest_framework import viewsets,pagination, exceptions, response,status
from vaccination.models import VaccinationChart
from vaccination.serializers import VaccinationSerializer
# Create your views here.
from django.views.generic.edit import FormMixin

from django.db.models import Count,Q
from django.shortcuts import render
from .models import VaccinationChart
from django.http import JsonResponse

def vaccine_page(request):
    return render(request,'vaccination/vaccine_year_wise.html')

from django.db.models.functions import TruncYear as Year
def vaccine_year_wise(request):
    dataset = VaccinationChart.objects.annotate(year=Year('date_of_vaccination')).values('year').annotate(
        count=Count('pk'))
    catgories , series_data = [],[]
    for record in dataset:
        catgories.append(str(record.get('year').year))
        series_data.append(record.get('count'))

    data = {
        'title': {
            'text': 'Chart reflow is set to true'
        },

        'subtitle': {
            'text': 'When resizing the window or the frame, the chart should resize'
        },

        'xAxis': {
            'categories': catgories
        },

        'series': [{
            'data': series_data
        }]
    }
    return JsonResponse(data)
