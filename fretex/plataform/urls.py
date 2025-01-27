from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.landing, 
        name='index'),

    path('login/', views.Login.as_view(), 
        name='login'),

    path('logout/', views.logoutView, 
        name='logout'),

    path('escolhacadastro/', views.escolhaCadastro, 
        name='escolhacadastro'),

    path('cadastrocliente/', views.CadastroCliente.as_view(), 
        name='cadastrocliente'),

    path('cadastrofreteiro/', views.CadastroFreteiro.as_view(),
        name='cadastrofreteiro'),

    path('fretes/', views.fretes_index, 
        name='fretes_index'),

    path('fretes/<int:pedido_id>/', views.fretes_show, 
        name='fretes_show'),

    path('proposta/', views.proposta_create, 
        name='proposta_create'),

    path('proposta/<int:proposta_id>/aceitar/', views.proposta_aceitar, 
        name='proposta_aceitar'),
    
    path('pedido/<int:pedido_id>/encerrar/', views.entrega_concluida, 
        name='entrega_concluida'),

    path('dashboardfreteiro/', views.dashboardFreteiro, 
        name='dashboardfreteiro'),

    path('dashboardcliente/', views.dashboardCliente, 
        name='dashboardcliente'),

    path('perfilCliente/', views.perfilCliente, 
        name="perfilCliente"),

    path('perfilFreteiro/', views.perfilFreteiro, 
        name="perfilFreteiro"),

    path('editarPerfilCliente/', views.EditarPerfilCliente.as_view(),
        name="editarPerfilCliente"),

    path('editarPerfilFreteiro/', views.EditarPerfilFreteiro.as_view(),
        name="editarPerfilFreteiro"),

    path('meusVeiculos/', views.meusVeiculos,
        name="meusVeiculos"),

    path('adicionarVeiculo/', views.AdicionarVeiculo.as_view(),
        name="adicionarVeiculo"),

    path('deletarVeiculo/<int:veiculo_id>', views.DeletarVeiculo, 
        name="deletarVeiculo"),

    path('cadastrofrete/', views.CadastroDeFrete.as_view(), 
        name="cadastrodefrete"),

    path('deletarPedido/<int:pedido_id>', views.DeletarPedido,
        name="deletarPedido"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
