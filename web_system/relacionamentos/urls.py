from django.urls import path
from relacionamentos.views.funcoes import primeira_view, saudacao, calculo, exercicio, nome
from relacionamentos.views import PrimeiraView, NomeView, SaudacaoView
from relacionamentos.views.reporter import reporter_list, reporter_detail, reporter_delete,reporter_gerar_codigo,create,update

app_name = 'relacionamentos'

urlpatterns = [
    
    path('funcao/teste', primeira_view,
         name='primeira_view'),
    
    path('funcao/saudacao', saudacao,
         name="saudacao"),

    path('funcao/exercicio/calculo/<int:x>/<int:y>', calculo,
         name="calculo"),
    
    path('funcao/exercicio/<str:nome>', exercicio,
         name='exercicio'),

    # Qualquer coisa em string, deve sempre ser por ultimo para nao inutilizar as urls de cima que sao fixas
    # nome é a variavel que vai armazenar o que vem depois de funcao/
    path('funcao/<str:nome>', nome,
         name="nome"),

    path('reporter/function/create',create,name="create_reporter"),

    path('reporter/function/read/<int:pk>', reporter_detail, name="reporter_read"), 
    
    path('reporter/function/delete/<int:pk>', reporter_delete, name="reporter_delete"),

    path('reporter/function/update/<int:reporter_id>',update,name="reporter_update"),

    path('reporter/function/gerar_codigo/<int:reporter_id>',reporter_gerar_codigo, name="reporter_gerar_codigo"),

    path('reporter/function/', reporter_list, name="reporter"), 

    path('classe/teste', PrimeiraView.as_view(), name="primeira_view_class"),
    
    path('classe/saudacao', SaudacaoView.as_view(), name="saudacao_view_class"),

    path('classe/<str:nome>', NomeView.as_view(), name="nome_view_class" ),


]