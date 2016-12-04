from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import *
from .models import *

flatten = lambda l: [item for sublist in l for item in sublist]

def findIll(sintomas):
    illness = []
    a = []
    for symptom in sintomas:
        if symptom != None:
            for j in symptom.objetocaracteristica_set.all():
                a.append(j.obj)
            illness.append(a)
            a = []
    return illness

def posibles(lista):
    if len(lista) > 1:
        aux = lista.pop(0)
        for i in lista:
            aux = set(aux) | set(i)
        print aux
    else:
        return lista[0]
    return list(aux)

def fuzzy(illness, symptoms ):
    t = 0
    points = len(illness)*[0.0]
    nIll = 0
    for i in illness:
        for j in i.objetocaracteristica_set.all():
            for s in symptoms:
                if s == j.fea:
                    points[nIll]+=1.0
                    t+=1.0
        nIll+=1
        print points

    for i in range(len(points)):
        div = points[i] / t
        div = 100 if div > 1 else div*100
        points[i] = [div,illness[i]]

    return points

def buscar(request):
    posibleEnfermedad = []
    form = formBuscar(request.POST or None)
    #print(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            symptoms = form.cleaned_data.values()
            a = findIll(symptoms)
            illness = posibles(a)

            if(len(illness) == 0):
                result = ["No se tiene informacion de la enfermedad"]
            else:
                result = fuzzy(illness, symptoms)


            return render(request,'sistemaExperto/index.html',{'form':form, 'enfermedad':result})
    return render(request,'sistemaExperto/index.html',{'form':form})
