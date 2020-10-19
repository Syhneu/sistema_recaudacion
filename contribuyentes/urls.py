from django.urls import path, include
from . import views

app_name = 'contribuyentes'
urlpatterns = [
    path('', views.CreateContribuyente.as_view(template_name='contribuyentes/registro.html'), name='registro')
]
