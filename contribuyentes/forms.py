from django import forms
from . import models

class ContribuyentesForm(forms.ModelForm):
    class Meta:
        model = models.RcContrib