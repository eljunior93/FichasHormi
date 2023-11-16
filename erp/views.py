import os
import uuid
from django.db import connections
from django.shortcuts import render, redirect
from decimal import Decimal
from datetime import datetime, timedelta
import json
import subprocess
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.conf import settings
# from FormatosHormi.Formatos import formatoVacunas

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

@login_required
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

    return JsonResponse({"error": "No se proporcionó un código de paciente"})

@login_required
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
                        "NumeroArchivo": row[30],

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
                    "NumeroArchivo": vistaficha["NumeroArchivo"],
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

@login_required
def tu_vista_de_impresion(request):
    if request.method == 'GET':
        nombre_empresa_vacuna = request.GET.get('nombre_empresa_vacuna')
        ruc = request.GET.get('ruc')
        historia_clinica = request.GET.get('historiaclinica')
        primer_apellido = request.GET.get('primerapellido')
        segundo_apellido = request.GET.get('segundoapellido')
        primer_nombre = request.GET.get('primernombre')
        segundo_nombre = request.GET.get('segundonombre')
        sexo = request.GET.get('sexo')
        ocupacion = request.GET.get('ocupacion')
        vacuna_tetano = 'Recibida'
        vacuna_hepatitis_a = ''
        vacuna_hepatitis_b = ''
        influenza_estacionaria = ''
        fiebre_amarilla = ''
        sarampion = ''
        datos_filas_json = request.GET.get('datos_filas')
        datos_filas = json.loads(datos_filas_json) if datos_filas_json else []

        for fila in datos_filas:
            # Accede a las propiedades de cada fila
            dosis = fila['dosis']
            fecha_str = fila['fecha']  # La fecha como cadena en formato 'YYYY-MM-DD'
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
            lote = fila['lote']
            esquema = fila['esquema']
            responsable = fila['responsable']
            establecimiento = fila['establecimiento']
            observaciones = fila['observaciones']

        connection = connections["empresa"]
        # Realizar la inserción en la base de datos
        with connection.cursor() as cursor:
            sql_query = """
                INSERT INTO vacunacion (
                    NombreEmpresa,
                    Ruc,
                    HistoriaClinica,
                    PrimerApellido,
                    SegundoApellido,
                    PrimerNombre,
                    SegundoNombre,
                    Sexo,
                    Ocupacion,
                    VacunaTetano,
                    VacunaHepatitisA,
                    VacunaHepatitisB,
                    InfluenzaEstacionaria,
                    FiebreAmarilla,
                    Sarampion
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """

            # Define los valores para los parámetros
            params = (
                nombre_empresa_vacuna, ruc, historia_clinica, primer_apellido, segundo_apellido, primer_nombre,
                segundo_nombre, sexo, ocupacion, vacuna_tetano, vacuna_hepatitis_a, vacuna_hepatitis_b,
                influenza_estacionaria, fiebre_amarilla, sarampion
            )

            # Ejecutar la consulta
            cursor.execute(sql_query, params)
            # Obtener el valor de numeroArchivo después de la inserción
            cursor.execute("SELECT TOP 1 numeroArchivo FROM Vacunacion ORDER BY numeroArchivo DESC;")
            numero_archivo_result = cursor.fetchone()
            numero_archivo = str(numero_archivo_result[0]) if numero_archivo_result else None

            # Realizar la inserción en la tabla DosisVacunaTetano
        with connection.cursor() as cursor:
            sql_query_dosis = """
                    INSERT INTO DosisVacunaTetano (
                        NumeroArchivo,
                        DosisNumero,
                        Fecha,
                        Lote,
                        EsquemaCompleto,
                        ResponsableVacuna,
                        Establecimiento,
                        Observaciones
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """

            # Define los valores para los parámetros en la tabla DosisVacunaTetano
            params_dosis = (
                numero_archivo,
                dosis, fecha, lote, esquema, responsable, establecimiento, observaciones
            )

            # Ejecutar la consulta para la tabla DosisVacunaTetano
            cursor.execute(sql_query_dosis, params_dosis)

        # Devolver todas las variables en la respuesta JSON
        response_data = {
            'nombre_empresa_vacuna': nombre_empresa_vacuna,
            'ruc': ruc,
            'historia_clinica': historia_clinica,
            'numero_archivo': numero_archivo,
            'primer_apellido': primer_apellido,
            'segundo_apellido': segundo_apellido,
            'primer_nombre': primer_nombre,
            'segundo_nombre': segundo_nombre,
            'sexo': sexo,
            'ocupacion': ocupacion,
            'vacuna_tetano': vacuna_tetano,
            'dosis_tetano': dosis,
            'fecha_tetano': fecha_str,
            'lote_tetano': lote,
            'esquema_tetano': esquema,
            'responsable_tetano': responsable,
            'establecimiento_tetano': establecimiento,
            'observaciones_tetano': observaciones

        }

        # Guardar los datos en un archivo JSON
        with open('postVacunas.json', 'w') as json_file:
            json.dump(response_data, json_file)

        # Obtén la ruta completa del script
        script_path = 'erp/FormatosHormi/Formatos/formatoVacunas.py'

        # Ejecutar el script de Python
        try:
            subprocess.run(['python', script_path])
        except Exception as e:
            print(f"Error al ejecutar el script: {e}")

        return JsonResponse(response_data)
        response['Content-Disposition'] = 'inline; filename="nombre_del_archivo.pdf"'
    else:
        return JsonResponse({'error': 'Método no permitido'})




