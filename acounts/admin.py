from django.contrib import admin
from .models import Pessoa

class CustomizandoAdmin(admin.ModelAdmin):
    list_display = ('texto','DataNasci', 'usuario_id')

admin.site.register(Pessoa, CustomizandoAdmin)