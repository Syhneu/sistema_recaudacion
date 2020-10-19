from django.shortcuts import render, redirect
from .models import rrcontrib
from contribuyentes.forms import RegistroContribuyente
# Create your views here.

def index(request):
  return render(request,'inicio.html')

def registroContribuyente(request):
  if request.method == 'POST':
    form = RegistroContribuyente(request.POST)
    if form.is_valid():
      form.save()
      return redirect('inicio.html')
  else:
    form = RegistroContribuyente()
    
  return render(request, 'registrocontribuyente.html', {'form': form})
