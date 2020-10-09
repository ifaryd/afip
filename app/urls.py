from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('acceuil', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('propos', views.propos, name='propos'),
    path('service', views.service, name='service'),
]