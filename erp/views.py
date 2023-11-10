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
        cursor.execute("SELECT Codprovcli,idprovcli as historia,RUC,Nombre,Direccion1,Telefono1, bandactivo  FROM Empleado e inner join personal p on e.idprovcli=p.idempleado  Where CODPROVCLI like '%%' ORDER BY Nombre")
        pcprovcli_results = cursor.fetchall()

        data = []
        for row in pcprovcli_results:
            data.append({
                'codprovcli': row[0],
            })
        username = request.user
        contexto = {
            'username': username,
        }
        print(data)
    return render(request, 'hormi2023.html',contexto)









