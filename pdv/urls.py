from django.urls import path
from . import views

urlpatterns = [
    # login - logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # clientes
    path('clientes/', views.clientes_view, name='clientes'),
    path('clientes/novo/', views.criar_cliente, name='criar_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),

    # reservas
    path('reservas/', views.reservas_view, name='reservas'),
    path('reservas/novo/', views.criar_reserva, name='criar_reserva'),
    path('reservas/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/excluir/<int:id>/', views.excluir_reserva, name='excluir_reserva'),

    # relatórios
    path('relatorios/', views.relatorios_view, name='relatorios'),

    # quartos
    path('quartos/', views.listar_quartos, name='listar_quartos'),
]