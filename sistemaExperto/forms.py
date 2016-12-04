from django import forms
from .models import *

class formBuscar(forms.Form):

    sintoma1 = forms.ModelChoiceField(required=False, queryset= caracteristica.objects.all().order_by('feature'))
    sintoma2 = forms.ModelChoiceField(required=False, queryset= caracteristica.objects.all().order_by('feature'))
    sintoma3 = forms.ModelChoiceField(required=False, queryset= caracteristica.objects.all().order_by('feature'))
    sintoma4 = forms.ModelChoiceField(required=False, queryset= caracteristica.objects.all().order_by('feature'))
