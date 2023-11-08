from django.urls import path
from erp import views
from sii_seguridad.vistas.autenticacion_vista import login, signout

from sii_seguridad import views

urlpatterns = [
    # URL para la página de inicio de sesión (login)
    path('', login ,name='login'),
    # URL para la página de cierre de sesión (logout)
    path('logout/', signout, name='logout'),
    path('empresa/', views.empresa, name='empresa'),


]
