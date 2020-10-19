from django.shortcuts import render
from django.views import generic
from .forms import ContribuyentesForm
from .models import RcContrib

# Create your views here.

class CreateContribuyente(generic.CreateView):
    model = RcContrib
    template = 'registro.html'
    form_class = ContribuyentesForm