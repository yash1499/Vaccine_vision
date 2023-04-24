from django.conf.urls import url

from . import views
from django.contrib.auth.views import login,logout
from rest_framework.routers import SimpleRouter
from accounts.apis import *
router=SimpleRouter()

router.register('doctor', DoctorView, base_name='doctor')
router.register('patient', PatientView, base_name='patient')

urlpatterns = [
    url('home-page/', views.home),
    url('search/',views.search,name='vaccine_search'),
    url('login/',login, {'template_name' : 'accounts/sign_in.html'},name='login'),
    url('logout/',logout, {'template_name' : 'accounts/logout.html'}),
    url('profile/',views.home1),
    url('heat/',views.results8,name='vaccine_map'),
]