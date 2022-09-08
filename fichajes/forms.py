from django.forms import ModelForm
from fichajes.models import Fichaje

class EntradaForm(ModelForm):
    class Meta:
        model = Fichaje
        fields = ['usuario']

class SalidaForm(ModelForm):
    class Meta:
        model = Fichaje
        fields = ['usuario']
