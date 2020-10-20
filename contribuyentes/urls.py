from django.urls import path, include
from . import views

app_name = 'contribuyentes'
urlpatterns = [
    path('registro/', views.registrar_contribuyente, name='registro')
]
