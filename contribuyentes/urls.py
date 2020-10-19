from django.urls import path, include
from . import views

app_name = 'contribuyentes'
urlpatterns = [
    path('contribuyentes/', views.CreateContribuyente.as_view(), name='registro')
]
