"""erp_ishida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from erp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        include(
            "sii_seguridad.urls",
        ),
    ),
    path("empresa/Hormi2023", views.hormi2023, name="hormi2023"),
    path(
        "empresa/Hormi2023/obtener_datos_paciente/",
        views.obtener_datos_paciente,
        name="obtener_datos_paciente",
    ),
    path("empresa/mq2010New/contact", views.contact, name="contact"),
    path("empresa/Hormi2023/fichasii4/", views.fichasii4, name="fichasii4"),
    path("empresa/Hormi2023/prueba/", views.tu_vista_de_impresion, name="tu_vista_de_impresion"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
