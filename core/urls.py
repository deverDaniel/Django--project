from django.urls import path,include
from .views import home,\
    lista_pessoas, lista_veiculos, lista_movrotativos, lista_mensalista, lista_movmensalista,\
    pessoa_novo, veiculo_novo, movrotativo_novo, mensalista_novo, movmensalista_novo,\
    pessoa_update, veiculo_update ,movrotativo_update, mensalista_update, movmensalista_update, \
    pessoa_delete, veiculo_delete, movrotativo_delete, mensalista_delete, movmensalista_delete
urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas', lista_pessoas, name= "core_lista_pessoa"), ##name funciona como um id para o redirect
    path('pessoa-novo', pessoa_novo, name= "core_pessoa_novo"),
    path('pessoa-update/<int:id>', pessoa_update, name= "core_pessoa_update"),
    path('pessoa-delete/<int:id>', pessoa_delete, name= "core_pessoa_delete"),


    path('veiculos', lista_veiculos, name= "core_lista_veiculo"),
    path('veiculos-novo', veiculo_novo, name= "core_veiculo_novo"),
    path('veiculos-update/<int:id>', veiculo_update, name= "core_veiculo_update"),
    path('veiculo-delete/<int:id>', veiculo_delete, name= "core_veiculo_delete"),


    path('mov-rot', lista_movrotativos, name= "core_lista_movrotativo"),
    path('mov-rot-novo', movrotativo_novo, name= "core_movrotativo_novo"),
    path('mov-rot-update/<int:id>', movrotativo_update, name= "core_movrotativo_update"),
    path('mov-rot-delete/<int:id>', movrotativo_delete, name= "core_movrotativo_delete"),


    path('mensalistas', lista_mensalista, name= "core_lista_mensalista"),
    path('mensalistas-novo', mensalista_novo, name= "core_mensalista_novo"),
    path('mensalistas-update/<int:id>', mensalista_update, name= "core_mensalista_update"),
    path('mensalista-delete/<int:id>', mensalista_delete, name= "core_mensalista_delete"),


    path('mov-mensalista', lista_movmensalista, name= "core_lista_movmensalista"),
    path('mov-mensalista-novo', movmensalista_novo, name= "core_movmensalista_novo"),
    path('mov-mensalista-update/<int:id>', movmensalista_update, name= "core_movmensalista_update"),
    path('movmensalista-delete/<int:id>', movmensalista_delete, name= "core_movmensalista_delete"),
]
