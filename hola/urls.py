"""hola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from fichajes.views import EntradaView, SalidaView, estado_fichaje, fichajes_de_usuario, hola, mis_fichajes

urlpatterns = [
    path('', hola, name="portada"),
    path('entrada', EntradaView.as_view(), name="entrada"),
    path('salida', SalidaView.as_view(), name="salida"),
    path('estado/<int:usuario_id>', estado_fichaje, name="estado"),
    path('admin/', admin.site.urls),
    path('fichajes', mis_fichajes, name='fichajes'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('fichajes_usuario/<int:usuario_id>', fichajes_de_usuario, name='fichajes_de_usuario')
]
