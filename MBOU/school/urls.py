from django.urls import path
from . import views

urlpatterns = [
    path('', views.glavnaya, name='glavnaya'),
    path('novosti/', views.novosti, name='novosti'),
    path('roditelyam/', views.roditelyam, name='roditelyam'),
    path('o-shkole/', views.oshkole, name='o-shkole'),
    path('uchebnaya-deyatelnost/', views.uchebnayadeyatelnost, name='uchebnaya-deyatelnost'),
    path('kontakty/', views.kontakty, name='kontakty'),
]