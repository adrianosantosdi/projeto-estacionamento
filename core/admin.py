from django.contrib import admin
from .models import Pessoa, Marca, Veiculo, Parametro, MovRotativo

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'placa', 'cor', 'observacoes')   


class ParametroAdmin(admin.ModelAdmin):
    list_display = ('valor_hora', 'valor_mes')  


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 'total', 'horas_total')


admin.site.register(Pessoa, PessoaAdmin)     
admin.site.register(Marca, MarcaAdmin)     
admin.site.register(Veiculo, VeiculoAdmin)     
admin.site.register(Parametro, ParametroAdmin)     
admin.site.register(MovRotativo, MovRotativoAdmin)     
