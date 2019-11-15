"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Formulario, Estudiante, Carrera, Catedratico, Curso, CursoLibre, AsignacionCurso, AsignacionCursoLibre, Publicacion
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/inicio.html',
        {
            'title':'Página Principal',
            'year':datetime.now().year,
        }
    )

def contacto(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':

        cont = Formulario()
        cont.nombre = request.POST['nombre']
        cont.email = request.POST['email']
        cont.mensaje = request.POST['mensaje']
        cont.save()
   

    return render(
        request,
        'app/contact.html',
        {
            'title':'Contacto',
            'message':'Información de Contacto',
            'year':datetime.now().year,
        }
    )

def acercade(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about-us.html',
        {
            'title':'Acerca de nosotros',
            'message':'Página de Descripción',
            'year':datetime.now().year,
        }
    )

def blog(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        cont= Publicacion()
        cont.titulo = request.POST['titulo']
        cont.nombre_prof = request.user
        cont.descripcion = request.POST['descripcion']
        cont.save()

    return render(
        request,
        'app/iblog.html',
        {
            'title':'Blog',
            'message':'Blog',
            'year':datetime.now().year,
        }
    )

class ListarPublicacionView(generic.ListView):
       template_name='app/blog.html'
       model=Publicacion

       def get_queryset(self):
           return Publicacion.objects.all()

def blogest(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        cont= Estudiante()
        cont.nombre = request.POST['nomest']
        cont.apellido = request.POST['apellido_est']
        cont.direccion = request.POST['direccion_est']
        cont.telefono = request.POST['telefono_est']
        cont.carnet = request.POST['carnet_est']
        cont.carrera_id = request.POST['carrera_est']
        cont.save()
    
    return render(
        request,
        'app/iblog_estudiante.html',
        {
            'title':'Blog',
            'message':'Blog',
            'year':datetime.now().year,
        }
    )

class ListarEstudianteView (generic.ListView):
    template_name = 'app/blog_estudiante.html'
    model=Estudiante
    
    def get_queryset(self):
        return Estudiante.objects.all()


def bloga(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        ca = Carrera()
        ca.id_Carrera = request.POST['carrera_carrera']
        ca.nombre = request.POST['nombre_carrera']
        ca.save()

    return render(
        request,
        'app/iblog_ingresarcarrera.html',
        {
            'title':'Blog',
            'message':'Blog',
            'year':datetime.now().year,
        }
    )

class ListarIngresarCarrera (generic.ListView):
    template_name = 'app/blog_ingresarcarrera.html'
    model=Carrera
    
    def get_queryset(self):
        return Carrera.objects.all()

def blogb(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        cat = Catedratico()
        cat.id_Catedratico = request.POST['id_cat']
        cat.nombre = request.POST['nombre_cat']
        cat.apellido = request.POST['apellido_cat']
        cat.telefono = request.POST['telefono_cat']
        cat.direccion = request.POST['direccion_cat']
        cat.save()

    return render(
        request,
        'app/iblog_agregarcatedratico.html',
        {
            'title':'Blog',
            'message':'Blog',
            'year':datetime.now().year,
        }
    )

class ListarIngresarCatedratico (generic.ListView):
    template_name = 'app/blog_agregarcatedratico.html'
    model=Catedratico
    
    def get_queryset(self):
        return Catedratico.objects.all()


def blogc(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        cur = Curso()
        cur.id_Curso = request.POST['id_curso']
        cur.nombre = request.POST['nombre_curso']
        cur.horario = request.POST['horario_curso']
        cur.catedratico_id = request.POST['catedratico_curso']
        cur.carrera_id = request.POST['carrera_curso']
        cur.save()

    return render(
        request,
        'app/iblog_ingresarcurso.html',
        {
            'title':'Blog',
            'message':'Blog',
            'year':datetime.now().year,
        }
    )

class ListarCurso (generic.ListView):
    template_name = 'app/blog_ingresarcurso.html'
    model=Curso
    
    def get_queryset(self):
        return Curso.objects.all()

def blogd(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        curl = CursoLibre()
        curl.id_CursoLibre = request.POST['id_cursolibre']
        curl.nombre = request.POST['nombre_cursolibre']
        curl.horario = request.POST['horario_cursolibre']
        curl.catedratico_id = request.POST['catedratico_cursolibre']
        curl.save()

    return render(
        request,
        'app/iblog_ingresarcursolibre.html',
        {
            'title':'Blog',
            'message':'Blog',
            'year':datetime.now().year,
        }
    )

class ListarCursoLibre (generic.ListView):
    template_name = 'app/blog_ingresarcursolibre.html'
    model=CursoLibre
    
    def get_queryset(self):
        return CursoLibre.objects.all()

def blog_asignacionA(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        asig = AsignacionCurso()
        asig.id_asignacion = request.POST['id_asignacion']
        asig.estudiante_id = request.POST['id_asignaestudiante']
        asig.curso_id = request.POST['id_asignacurso']
        asig.save()
        

    return render(
        request,
        'app/iblog_cursocarrera.html',
        {
            'title':'Blog',
            'message':'Blog',
            'year':datetime.now().year,
        }
    )

class ListarAsignaA (generic.ListView):
    template_name = 'app/blog_cursocarrera.html'
    model=AsignacionCurso
    
    def get_queryset(self):
        return AsignacionCurso.objects.all()

def blog_asignacionB(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        asigA = AsignacionCursoLibre()
        asigA.id_asignacionlibre = request.POST['id_asignacionl']
        asigA.estudiante_id = request.POST['id_asignaestudiantelibre']
        asigA.cursolibre_id = request.POST['id_asignacursolibre']
        

    return render(
        request,
        'app/iblog_cursolibre.html',
        {
            'title':'Blog',
            'message':'Blog',
            'year':datetime.now().year,
        }
    )

class ListarAsignaB (generic.ListView):
    template_name = 'app/blog_cursolibre.html'
    model=AsignacionCursoLibre
    
    def get_queryset(self):
        return AsignacionCursoLibre.objects.all()

def curso(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/course.html',
        {
            'title':'Cursos',
            'message':'Información sobre los Cursos',
            'year':datetime.now().year,
        }
    )

def cursolibre(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cursos_libres.html',
        {
            'title':'Cursos Libres',
            'message':'Información sobre los Cursos Libres',
            'year':datetime.now().year,
        }
    )

"""
def elementos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/elements.html',
        {
            'title':'Elementos',
            'year':datetime.now().year,
        }
    )
"""

"""
def login(request):
   
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html',
        {
            'title':'Login',
            'year':datetime.now().year,
        }
    )
"""


    
def login_registrar(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)


    return render(
        request,
        'app/login_registrar.html',
        {
            'title':'registrarse',
            'message':'Información de registro',
            'year':datetime.now().year,
        }
    )


def login_registrar_guardar(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        user=User.objects.create_user(request.POST['usuario'],'',request.POST['contraseña'])
        user.save()

        user=authenticate(username=(request.POST['usuario']),password=(request.POST['contraseña']))
        if user is not None:
         login(request,user)
            
        return render(
        request,
        'app/inicio.html',
        {
            'title':'inicio',
            'message':'Información de registro',
            'year':datetime.now().year,
         
        }
    )


def loginview(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)


    return render(
        request,
        'app/login.html',
        {
            'title':'login',
            'message':'Información de inicio',
            'year':datetime.now().year,
        }
    )

def login_guardar(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
     
        
        user=authenticate(request,username=(request.POST['usuario']),password=(request.POST['contraseña']))
        if user is not None:
          login(request,user)
        return render(
        request,
        'app/inicio.html',
        {
            'title':'inicio',
            'message':'Información de registro',
            'year':datetime.now().year,
         
        }
    )


def login_salir(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    logout(request)
    return render(
        request,
        'app/inicio.html',
        {
            'title':'inicio',
            'message':'inicio',
            'year':datetime.now().year,
        }
    )
