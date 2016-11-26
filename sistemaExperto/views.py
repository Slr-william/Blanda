from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import *
from .models import *

def findIll(sintomas):
    #print "----------------"
    #print sintomas
    #print sintomas[0].feature
    #print "-----------------"
    illness = []
    a = []
    for symptom in sintomas:
        for j in symptom.objetocaracteristica_set.all():
            a.append(j.obj.name)
        illness.append(a)
        a = []
    return illness

def inter(lista):
    #print "----------------"
    #print lista
    #print "-----------------"
    result = list(set(lista[0]).intersection(*lista))
    return result

def buscar(request):
    posibleEnfermedad = []
    form = formBuscar(request.POST or None)
    print(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            a = findIll(form.cleaned_data.values())
            r = inter(a)
            if(len(r) == 0):
                r.append("No se tiene informacion de la enfermedad")


            return render(request,'sistemaExperto/index.html',{'form':form, 'enfermedad':r})
    return render(request,'sistemaExperto/index.html',{'form':form})
