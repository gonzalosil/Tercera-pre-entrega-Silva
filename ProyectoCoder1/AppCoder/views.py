from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.models import Estudiante
from AppCoder.models import Profesor
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario
from AppCoder.forms import EstudianteFormulario
from AppCoder.forms import ProfesorFormulario
# Create your views here.


def inicio(request):

    return render(request, "AppCoder/inicio.html")


def cursos(request):

    return render(request, "AppCoder/cursos.html")


def profesores(request):

    return render(request, "AppCoder/profesores.html")


def estudiantes(request):

    return render(request, "AppCoder/estudiantes.html")


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
        camada = request.GET.get('camada')
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def estudianteFormulario(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)  # Aquí llega toda la información del HTML
        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion ["email"])
            estudiante.save()
            return render(request, "AppCoder/inicio.html")  # Vuelvo al inicio o a donde quieran
    else:
        miFormulario = EstudianteFormulario()  # Formulario vacío para construir el HTML
    return render(request, "AppCoder/estudiantesFormulario.html", {"miFormulario":miFormulario})


def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)  # Aquí llega toda la información del HTML
        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion ["email"], profesion = informacion ["profesion"])
            profesor.save()
            return render(request, "AppCoder/inicio.html")  # Vuelvo al inicio o a donde quieran
    else:
        miFormulario = ProfesorFormulario()  # Formulario vacío para construir el HTML
    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})