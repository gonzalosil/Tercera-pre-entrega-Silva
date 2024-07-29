from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.inicio),
    path('inicio', views.inicio),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('cursoFormulario', views.cursoFormulario),
    path('estudianteFormulario', views.estudianteFormulario),
    path('profesorFormulario', views.profesorFormulario),
    path('busquedaCamada', views.busquedaCamada),
    path('buscar/', views.buscar),
]