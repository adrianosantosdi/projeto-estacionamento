from django.urls import path
from .views import (index, pessoa, veiculo, lista_movrotativos, mensalista, mov_mensalista,
                     pessoa_novo, veiculo_novo, movrotativos_novo, mensalista_novo, mov_mensalista_novo,
                     pessoa_update, veiculo_update, movrotativo_update, mensalista_update, movmensalista_update,
                     pessoa_delete, veiculo_delete, movrotativo_delete, mensalista_delete, movmensalista_delete)


urlpatterns = [
    path('', index, name='index'),
    path('pessoas/', pessoa, name='pessoa'),
    path('pessoa_novo/', pessoa_novo, name='pessoa_novo'),
    path('pessoa-update/<int:id>', pessoa_update, name='pessoa_update'),
    path('pessoa-delete/<int:id>', pessoa_delete, name='pessoa_delete'),
    path('veiculos/', veiculo, name='veiculo'),
    path('veiculos-novo/', veiculo_novo, name='veiculo_novo'),
    path('veiculo-update/<int:id>', veiculo_update, name='veiculo_update'),
    path('veiculo-delete/<int:id>', veiculo_delete, name='veiculo_delete'),
    path('mov-rot/', lista_movrotativos, name='mov_rot'),
    path('mov-root-update/<int:id>', movrotativo_update, name='movrotativo_update'),
    path('mov-root-delete/<int:id>', movrotativo_delete, name='movrotativo_delete'),
    path('mov-rot-novo/', movrotativos_novo, name='movrotativos_novo'),
    path('mensalista/', mensalista, name='mensalista'),
    path('mensalista-novo/', mensalista_novo, name='mensalista_novo'),
    path('mensalista-update/<int:id>', mensalista_update, name='mensalista_update'),
    path('mensalista-delete/<int:id>', mensalista_delete, name='mensalista_delete'),
    path('mov-mensal/', mov_mensalista, name='mov_mensalista'),
    path('mov-mensal-novo/', mov_mensalista_novo, name='mov_mensalista_novo'),
    path('mov-mensal-update/<int:id>', movmensalista_update, name='movmensalista_update'),
    path('mov-mensal-delete/<int:id>', movmensalista_delete, name='movmensalista_delete'),
]