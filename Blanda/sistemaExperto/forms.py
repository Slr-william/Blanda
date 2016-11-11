from django import forms
from .models import *

class formBuscar(forms.Form):

    c1 = forms.ModelChoiceField(required=True, queryset= caracteristica.objects.all())
    c2 = forms.ModelChoiceField(required=True, queryset= caracteristica.objects.all())
    c3 = forms.ModelChoiceField(required=True, queryset= caracteristica.objects.all())
    c4 = forms.ModelChoiceField(required=True, queryset= caracteristica.objects.all())
