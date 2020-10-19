from django.shortcuts import render
from django.views import generic
from .forms import ContribuyentesForm
from .models import RcContrib, RcAccionistas, RcRepresentante

# Create your views here.

def index(request):
    return render(request, 'index.html')

class CreateContribuyente(generic.CreateView):
    model = RcContrib
    template = 'contribuyentes/registro.html'
    form_class = ContribuyentesForm