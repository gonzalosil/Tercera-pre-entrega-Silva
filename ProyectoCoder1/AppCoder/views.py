from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario
# Create your views here.


def inicio(request):

    return render(request, "AppCoder/inicio.html")


def cursos(request):

    return render(request, "AppCoder/cursos.html")


def profesores(request):

    return render(request, "AppCoder/profesores.html")


def estudiantes(request):

    return render(request, "AppCoder/estudiantes.html")


def entregables(request):

    return render(request, "AppCoder/entregables.html")


def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)  # Aquí llega toda la información del HTML
        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")  # Vuelvo al inicio o a donde quieran
    else:
        miFormulario = CursoFormulario()  # Formulario vacío para construir el HTML
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})


def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")


def buscar(request):
    if request.GET.get('camada'):
        # respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada = request.GET.get('camada')
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos"
        # No olvidar from django.http import HttpResponse
        return HttpResponse(respuesta)

# def curso(self):
#     curso = Curso(nombre="Desarrollo web", camada="19881")
#     curso.save()
#     documentoDeTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"

#     return HttpResponse(documentoDeTexto)