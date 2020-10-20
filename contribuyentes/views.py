from django.shortcuts import render
from django.views import generic
from .forms import ContribuyentesForm
from .models import RcContrib, RcAccionistas, RcRepresentante

# Create your views here.

#class CreateContribuyente(generic.CreateView):
#    model = RcContrib
#    template = 'registro.html'
#    form_class = ContribuyentesForm

# Probando con Function Based View
def registrar_contribuyente(request):

    if request.method == 'POST':
        pass

        # if valido
        # save
        
        # else
        # print error
    else:
        pass

    return render(request, 'contribuyentes/registro.html', {
        # formulario1: nombre_formulario,
        # formulario2: nombre_formulario,
    })