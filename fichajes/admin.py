from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from fichajes.models import Fichaje
from django.utils.html import format_html
from django.urls import reverse

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


class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin,self).__init__(*args, **kwargs)
        UserAdmin.list_display = list(UserAdmin.list_display) + ['fichajes']

    # Function to count objects of each user from another Model (where user is FK)
    def fichajes(self, obj):
        return format_html(
            '<a href="{}">Fichajes</a>',
            reverse('fichajes_de_usuario', args=[obj.id])
        )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)