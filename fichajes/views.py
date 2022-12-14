from datetime import date, datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from fichajes.forms import EntradaForm, SalidaForm
from fichajes.models import Fichaje
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

# Create your views here.
def hola(request):
    return render(request, 'portada.html', {'now':datetime.now()})


class EntradaView(View):
    # Carga de página con formulario
    def get(self, request):
        formulario = EntradaForm()
        return render(request, 'entrada.html',
            {'formulario':formulario})

    # Envío de datos del formulario    
    def post(self, request):
        formulario = EntradaForm(request.POST) 
        try:
            usuario_id = request.POST.get('usuario')
            fichaje = Fichaje.objects.filter(usuario_id=usuario_id).filter(salida=None).order_by('-entrada').first()
            if fichaje:
                raise Exception('Ya hay fichaje de entrada activo para ese usuario')            
            fichaje = Fichaje(entrada=datetime.now())
            formulario.instance = fichaje
            if formulario.is_valid():
                fichaje = formulario.save()
                return redirect('estado', fichaje.usuario_id)
            else:
                raise Exception('Datos no válidos')
        except Exception as error:
            formulario.add_error(None, error)
            return render(request, 'entrada.html', {'formulario':formulario})



def estado_fichaje(request, usuario_id):
    # Obtención del registro más reciente del usuario
    fichaje = Fichaje.objects\
        .filter(usuario_id=usuario_id)\
        .order_by('-entrada')\
        .first()
    return render(request, 'estado.html',
        {'fichaje': fichaje})


class SalidaView(View):
    # Carga de página con formulario
    def get(self, request):
        formulario = SalidaForm()
        return render(request, 'salida.html',
            {'formulario':formulario})

    # Envío de datos del formulario    
    def post(self, request):
        formulario = SalidaForm(request.POST)
        try:
            usuario_id = request.POST.get('usuario')
            fichaje = Fichaje.objects.filter(usuario_id=usuario_id).filter(salida=None).order_by('-entrada').first()
            if not fichaje:
                raise Exception("No hay fichaje de entrada previo")
            fichaje.salida = datetime.now()
            formulario.instance = fichaje
            if formulario.is_valid():
                fichaje = formulario.save()
                return redirect('estado', fichaje.usuario_id)
            else:
                raise Exception("Datos no válidos")
        except Exception as error:
            formulario.add_error(None, error)
            return render(request, 'salida.html', {'formulario':formulario})


@login_required
def mis_fichajes(request):
    fichajes = Fichaje.objects\
        .filter(usuario=request.user).all()
    return render(request, 'mis_fichajes.html', {
        'usuario': request.user,
        'fichajes': fichajes
    })


@staff_member_required
def fichajes_de_usuario(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    fichajes = Fichaje.objects\
        .filter(usuario=usuario).all()
    return render(request,'fichajes_usuario.html',{
        'usuario': usuario,
        'fichajes': fichajes
    })