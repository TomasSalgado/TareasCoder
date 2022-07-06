from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiar
# Create your views here.


def Familiares(self):

    familiar1= Familiar(nombref="Franco", fecha_nacimiento="1969-11-20", Edad=52)
    familiar1.save
    texto= f"Familiar creado: {familiar1.nombref} {familiar1.fecha_nacimiento} {familiar1.Edad}"
    return HttpResponse(texto)

def Familiares2(self):
    
    familiar2= Familiar(nombref="Juani", fecha_nacimiento="2000-07-23", Edad=21)
    familiar2.save
    texto= f"Familiar creado: {familiar2.nombref} {familiar2.fecha_nacimiento} {familiar2.Edad}"
    return HttpResponse(texto)

def Familiares3(self):
    
    familiar3= Familiar(nombref="Martin", fecha_nacimiento="1998-02-23", Edad=24)
    familiar3.save
    texto= f"Familiar creado: {familiar3.nombref} {familiar3.fecha_nacimiento} {familiar3.Edad}"
    return HttpResponse(texto)