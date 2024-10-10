from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro),#chama o views cadastro para cadastrar
    path('cadastro/', views.cadastro, name='cadastro'), #chama o views cadastro para cadastrar
    path('login/', views.login, name='login'), #chama o views login para logar
    path('dashboard/', views.dashboard, name='dashboard'), #chama o views dashboard para ver os dados e edita-los
    path('logout/', views.login, name='logout'), #chama o views dashboard para ver os dados e edita-los
]
