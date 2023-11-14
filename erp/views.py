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
                    "SELECT * FROM vw_infoempleado vw WHERE vw.CODPROVCLI = %s",
                    [codprovcli],
                )
                resultados = cursor.fetchall()

                vistaficha = {}
                for row in resultados:
                    vistaficha = {
                        "CodProvCli": row[0],
                        "Cedula": row[2],
                        "Sexo": row[3],
                        "EstadoCivil": row[4],
                        "PrimerApellido": row[5],
                        "SegundoApellido": row[6],
                        "PrimerNombre": row[7],
                        "SegundoNombre": row[8],
                        "DireccionActual": row[9],
                        "Telefono1": row[10],
                        "Telefono2": row[11],
                        "Email": row[12],
                        "Sector": row[13],
                        "FechaNacimiento": row[14],
                        "Edad": row[15],
                        "Grupo1": row[16],
                        "Grupo2": row[17],
                        "Grupo3": row[18],
                        "Instruccion": row[19],
                        "Profesion": row[20],
                        "Ocupacion": row[21],
                        "Provincia": row[22],
                        "Canton": row[23],
                        "Religion": row[24],
                        "Nacionalidad": row[25],
                        "Discapacidad": row[26],
                        "Tabaco": row[27],
                        "Alcohol": row[28],
                        "Droga": row[29],

                    }

                cursor.execute(
                    "SELECT TOP 1 Nombreempresa, ruc FROM gnopcion"
                )
                empresa_resultado = cursor.fetchone()

                empresa_data = {
                    "Nombreempresa": empresa_resultado[0],
                    "Ruc": empresa_resultado[1],
                    "HistoriaClinica": vistaficha["Cedula"],
                    "PrimerApellido": vistaficha["PrimerApellido"],
                    "SegundoApellido": vistaficha["SegundoApellido"],
                    "PrimerNombre": vistaficha["PrimerNombre"],
                    "SegundoNombre": vistaficha["SegundoNombre"],
                    "Sexo": vistaficha["Sexo"],
                    "Ocupacion": vistaficha["Ocupacion"],
                }

                return JsonResponse({"vistaficha": vistaficha, "empresa": empresa_data})

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
