from django.contrib import admin

from fichajes.models import Fichaje

admin.site.site_header = "Control de fichajes"

# Register your models here.
#admin.site.register(Fichaje)

@admin.register(Fichaje)
class FichajeAdmin(admin.ModelAdmin):
    list_display = (
        'usuario', 
        'entrada', 
        'salida'
    )