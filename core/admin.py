from django.contrib import admin
from .models import Marca, \
    Veiculo,\
    Pessoa,\
    Parametros,\
    MovRotativo, \
    Mensalista, \
    MovMensalista
class MovRotativoadm(admin.ModelAdmin):
    list_display = ('veiculo', 'entrada', 'saida', 'valor_hora', 'pago', 'total')

    def veeiculo(self,obj):
        return obj.veiculo

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pagamento', 'valor_mes')

admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoadm)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)


# Register your models here.
