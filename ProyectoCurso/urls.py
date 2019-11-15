"""
Definition of urls for ProyectoCurso.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('acercade/', views.acercade, name='acercade'),
    
    path('bloga/', views.blog, name='blogp'),
    path('blog/', views.ListarPublicacionView.as_view(extra_context={'title': 'Blog', 'year':datetime.now().year}), name='blog'),

    path('blog/est', views.blogest, name='blog_est'),
    path('blog/estudiantes', views.ListarEstudianteView.as_view(extra_context={'title': 'BlogEst', 'year':datetime.now().year}), name='blog_estudiante'),

    path('blog/car', views.bloga, name='blog_inc'),
    path('blog/carrera', views.ListarIngresarCarrera.as_view(extra_context={'title': 'BlogCar', 'year':datetime.now().year}), name='blog_ingresarcarrera'),


    path('blog/cat', views.blogb, name='blog_agregarcat'),
    path('blog/catedraticos', views.ListarIngresarCatedratico.as_view(extra_context={'title': 'BlogCat', 'year':datetime.now().year}), name='blog_agregarcatedratico'),


    path('blog/cur', views.blogc, name = 'blog_incur'),
    path('blog/cursos', views.ListarCurso.as_view(extra_context={'title': 'BlogCur', 'year':datetime.now().year}), name = 'blog_ingresarcurso'),


    path('blog/curlib', views.blogd, name = 'blog_incurlib'),
    path('blog/cursoslibres', views.ListarCursoLibre.as_view(extra_context={'title': 'BlogCurLib', 'year':datetime.now().year}), name = 'blog_ingresarcursolibre'),


    path('blog/asignacc', views.blog_asignacionA, name = 'blog_cc'),
    path('blog/asignacursocarrera', views.ListarAsignaA.as_view(extra_context={'title': 'BlogAsign', 'year':datetime.now().year}), name = 'blog_cursocarrera'),



    path('blog/asignacl', views.blog_asignacionB, name = 'blog_cl'),
    path('blog/asignacursolibre', views.ListarAsignaB.as_view(extra_context={'title': 'BlogAsignLib', 'year':datetime.now().year}), name = 'blog_cursolibre'),



    path('cursos/', views.curso, name='cursos'),    
    path('cursoslibres/', views.cursolibre, name='cursolibre'),

    path('login/',views.loginview, name='login'), 
    path('login_salir/',views.login_salir, name='login_salir'),
    path('login_guardar/',views.login_guardar, name='login_guardar'),
    path('login_registrar_guardar/',views.login_registrar_guardar, name='login_registrar_guardar'),
    path('login_registrar/',views.login_registrar, name='login_registrar'),

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]