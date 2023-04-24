from rest_framework.routers import SimpleRouter
from django.conf.urls import url, include
from django.conf.urls import url
from .views import *

router=SimpleRouter()
urlpatterns  = [
    url('vaccine-year-wise/', vaccine_year_wise,name='vaccine_year_wise'),
    url('vaccine-year-wise-page/', vaccine_page)
]

