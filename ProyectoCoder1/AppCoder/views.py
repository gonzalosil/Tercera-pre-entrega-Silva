from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
# Create your views here.


def inicio(request):

    return HttpResponse('Vista inicio')


def cursos(request):

    return HttpResponse('Vista cursos')


def profesores(request):

    return HttpResponse('vista profesores')


def estudiantes(request):

    return HttpResponse('Vista estudiantes')


def entregables(request):

    return HttpResponse('Vista entregables')
# def curso(self):
#     curso = Curso(nombre="Desarrollo web", camada="19881")
#     curso.save()
#     documentoDeTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"

#     return HttpResponse(documentoDeTexto)