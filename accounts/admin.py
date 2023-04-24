from django.contrib import admin
from vaccination.models import VaccinationChart
from accounts.models import Doctor,Patient

admin.site.register(VaccinationChart)
admin.site.register(Doctor)


from import_export import resources
from .models import Patient
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin

class PatientResource(resources.ModelResource):
    class Meta:
        model = Patient

class PatientAdmin(ImportExportModelAdmin):
    resource_class = PatientResource


admin.site.register(Patient,PatientAdmin)

def export(request):
    person_resource = PatientResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response



from django.dispatch import receiver
from import_export.signals import post_import, post_export

@receiver(post_import, dispatch_uid='balabala...')
def _post_import(model, **kwargs):
    # model is the actual model instance which after import
    pass

@receiver(post_export, dispatch_uid='balabala...')
def _post_export(model, **kwargs):
    # model is the actual model instance which after export
    pass