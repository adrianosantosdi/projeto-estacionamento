from django.contrib import admin
from .models import Pessoa, Marca, Veiculo, Parametro, MovRotativo, Mensalista, MovMensalista

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'placa', 'cor', 'observacoes')   


class ParametroAdmin(admin.ModelAdmin):
    list_display = ('valor_hora', 'valor_mes')  


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 'total', 'horas_total', 'veiculo')

    def veiculo(self, obj): 
        return obj.veiculo
    
    
class MensalistaAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'inicio', 'valor_mes')  


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pago', 'total')      


admin.site.register(Pessoa, PessoaAdmin)     
admin.site.register(Marca, MarcaAdmin)     
admin.site.register(Veiculo, VeiculoAdmin)     
admin.site.register(Parametro, ParametroAdmin)     
admin.site.register(MovRotativo, MovRotativoAdmin)     
admin.site.register(Mensalista, MensalistaAdmin)     
admin.site.register(MovMensalista, MovMensalistaAdmin)     
