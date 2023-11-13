import os
import uuid
from django.db import connections
from django.shortcuts import render,redirect
from decimal import Decimal
from datetime import datetime, timedelta
import json
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.conf import settings

# Función para convertir objetos Decimal a números de punto flotante (float)
from erp_ishida.settings import BASE_DIR


# Principal
@login_required
def hormi2023(request):
    connection = connections['empresa']
    with connection.cursor() as cursor:
        cursor.execute("	SELECT  pc.CodProvCli, pc.Nombre FROM Empleado pc  Inner join personal p on p.idempleado = pc.idprovcli  Where BandGestion=0 and pc.nombre LIKE '%%' ORDER BY pc.Nombre")
        pcprovcli_results = cursor.fetchall()

        data = []
        for row in pcprovcli_results:
            data.append({
                'codprovcli': row[0],
                'nombre': row[1],
            })
        username = request.user
        contexto = {
            'data': data,
            'username': username,
        }

    return render(request, 'hormi2023.html',contexto)


# Obtener apcientes por del codprovclijson
def obtener_datos_paciente(request):
    codprovcli = request.GET.get('codprovcli', None)


    if codprovcli:
        connection = connections['empresa']
        with connection.cursor() as cursor:
            cursor.execute("SELECT Codprovcli, idprovcli as historia, RUC, Nombre, Direccion1, Telefono1, bandactivo FROM Empleado e INNER JOIN personal p ON e.idprovcli=p.idempleado WHERE CODPROVCLI = %s ORDER BY Nombre", [codprovcli])
            resultados = cursor.fetchall()

        data = []
        for row in resultados:
            data.append({
                'codprovcli': row[0],
                'historia': row[1],
                'ruc': row[2],
                'nombre': row[3],
                'direccion': row[4],
                'telefono': row[5],
                'bandactivo': row[6],
            })

        return JsonResponse({'data': data})
        print(data)
    return JsonResponse({'error': 'No se proporcionó un código de paciente'})



def fichasii4(request):
    codprovcli = request.GET.get('codprovcli', None)

    if codprovcli:
        connection = connections['empresa']
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM vwEmpleado  WHERE CODPROVCLI = %s",
                [codprovcli])
            resultados = cursor.fetchall()

        vistaficha = []
        for row in resultados:
            vistaficha.append({
                'IdProvCli': row[0],
                'CodProvCli': row[1],
                'Nombre': row[2],

            })

        return JsonResponse({'vistaficha': vistaficha})
        print(vistaficha)
    return JsonResponse({'error': 'No se proporcionó un código de paciente'})


@login_required
def contact(request):
    username = request.user

    context = {
        'username': username
    }
    return render(request, 'contact.html', context)





