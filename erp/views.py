import os
import uuid
from django.db import connections
from django.shortcuts import render, redirect
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
    connection = connections["empresa"]
    with connection.cursor() as cursor:
        cursor.execute(
            "	SELECT  pc.CodProvCli, pc.Nombre FROM Empleado pc  Inner join personal p on p.idempleado = pc.idprovcli  Where BandGestion=0 and pc.nombre LIKE '%%' ORDER BY pc.Nombre"
        )
        pcprovcli_results = cursor.fetchall()

        data = []
        for row in pcprovcli_results:
            data.append(
                {
                    "codprovcli": row[0],
                    "nombre": row[1],
                }
            )
        username = request.user
        contexto = {
            "data": data,
            "username": username,
        }

    return render(request, "hormi2023.html", contexto)


# Obtener apcientes por del codprovclijson
def obtener_datos_paciente(request):
    codprovcli = request.GET.get("codprovcli", None)

    if codprovcli:
        connection = connections["empresa"]
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT Codprovcli, idprovcli as historia, RUC, Nombre, Direccion1, Telefono1, bandactivo FROM Empleado e INNER JOIN personal p ON e.idprovcli=p.idempleado WHERE CODPROVCLI = %s ORDER BY Nombre",
                [codprovcli],
            )
            resultados = cursor.fetchall()

        data = []
        for row in resultados:
            data.append(
                {
                    "codprovcli": row[0],
                    "historia": row[1],
                    "ruc": row[2],
                    "nombre": row[3],
                    "direccion": row[4],
                    "telefono": row[5],
                    "bandactivo": row[6],
                }
            )

        return JsonResponse({"data": data})
        print(data)
    return JsonResponse({"error": "No se proporcionó un código de paciente"})


def fichasii4(request):
    codprovcli = request.GET.get("codprovcli", None)

    if codprovcli:
        connection = connections["empresa"]
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    "select * from vw_infoempleado vw WHERE vw.CODPROVCLI = %s",
                    [codprovcli],
                )

                resultados = cursor.fetchall()

                vistaficha = []
                for row in resultados:
                    vistaficha.append(
                        {
                            "CodProvCli": row[0],
                            "HistoriaClinica": row[1],
                            "Cedula": row[2],
                            "Sexo": row[3],
                            "EstadoCivil": row[4],
                            "Nombre": row[5],
                            "Apellido": row[6],
                            "DireccionActual": row[7],
                            "Telefono1": row[8],
                            "Telefono2": row[9],
                            "Email": row[10],
                            "Sector": row[
                                11
                            ],  # Asegúrate de que esta columna esté seleccionada correctamente
                            "FechaNacimiento": row[12],
                            "Edad": row[13],
                            "Grupo1": row[14],
                            "Grupo2": row[15],
                            "Grupo3": row[16],
                            "Instruccion": row[17],
                            "Profesion": row[18],
                            "Ocupacion": row[19],
                            "Provincia": row[20],
                            "Canton": row[21],
                            "Religion": row[22],
                            "Nacionalidad": row[23],
                            "Discapacidad": row[24],
                            "Tabaco": row[25],
                            "Alcohol": row[26],
                            "Droga": row[27],
                        }
                    )

                return JsonResponse({"vistaficha": vistaficha})

            except Exception as e:
                return JsonResponse(
                    {"error": f"Error al ejecutar la consulta: {str(e)}"}
                )

    return JsonResponse({"error": "No se proporcionó un código de paciente"})


@login_required
def contact(request):
    username = request.user

    context = {"username": username}
    return render(request, "contact.html", context)
