from django.urls import path
from contribuyentes import views

urlpatterns = [
  path("registrocontribuyente/", views.index, name="index")
]
