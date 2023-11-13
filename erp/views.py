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
from django.core.files.storage import default_storage
from django.conf import settings

# Función para convertir objetos Decimal a números de punto flotante (float)
from erp_ishida.settings import BASE_DIR


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
        print(data)
    return render(request, 'hormi2023.html',contexto)



@login_required
def contact(request):
    username = request.user

    context = {
        'username': username
    }
    return render(request, 'contact.html', context)





