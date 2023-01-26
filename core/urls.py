from django.urls import path 
from .views import home,api,ayudanos,galeria,gatos,quienes,mostrar, eliminar, crear,modificar, mostrarCli, eliminarCli, crearCli, modificarCli


urlpatterns=[
    path('', home, name="home"),
    path('api/', api, name="api"),
    path('ayudanos/', ayudanos, name="ayudanos"),
    path('galeria/',galeria, name="galeria"),
    path('gatos/', gatos, name="gatos"),
    path('quienes/', quienes, name="quienes"),
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('crear/',crear, name="crear"),
    path('modificar/<id>', modificar, name="modificar"),
    path('mostrarCli/', mostrarCli, name="mostrarCli"),
    path('eliminarCli/<id>', eliminarCli, name="eliminarCli"),
    path('crearCli/',crearCli, name="crearCli"),
    path('modificarCli/<id>', modificarCli, name="modificarCli"),
       
]