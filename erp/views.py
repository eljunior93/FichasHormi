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
                vistaficha = {"dosis": []}

                for row in resultados:
                    dosis_actual = {
                        "NumeroArchivo": row[30],
                        "Id_dosistetano": row[31],
                        "NumeroArchivofk": row[32],
                        "DosisTetano": row[33],
                        "FechaTetano": row[34],
                        "Lotetetano": row[35],
                        "Esquematetano": row[36],
                        "ResponsableVacunaTetano": row[37],
                        "EstablecimientoTetano": row[38],
                        "Observaciones": row[39],
                    }
                    vistaficha["dosis"].append(dosis_actual)

                vistaficha.update({
                    "CodProvCli": resultados[0][0],
                    "Cedula": resultados[0][2],
                    "Sexo": resultados[0][3],
                    "EstadoCivil": resultados[0][4],
                    "PrimerApellido": resultados[0][5],
                    "SegundoApellido": resultados[0][6],
                    "PrimerNombre": resultados[0][7],
                    "SegundoNombre": resultados[0][8],
                    "DireccionActual": resultados[0][9],
                    "Telefono1": resultados[0][10],
                    "Telefono2": resultados[0][11],
                    "Email": resultados[0][12],
                    "Sector": resultados[0][13],
                    "FechaNacimiento": resultados[0][14],
                    "Edad": resultados[0][15],
                    "Grupo1": resultados[0][16],
                    "Grupo2": resultados[0][17],
                    "Grupo3": resultados[0][18],
                    "Instruccion": resultados[0][19],
                    "Profesion": resultados[0][20],
                    "Ocupacion": resultados[0][21],
                    "Provincia": resultados[0][22],
                    "Canton": resultados[0][23],
                    "Religion": resultados[0][24],
                    "Nacionalidad": resultados[0][25],
                    "Discapacidad": resultados[0][26],
                    "Tabaco": resultados[0][27],
                    "Alcohol": resultados[0][28],
                    "Droga": resultados[0][29],
                    "NumeroArchivo": resultados[0][30],
                    "PuestoTrabajo": resultados[0][31],

                })

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

                return JsonResponse({"dosistetano": vistaficha, "empresa": empresa_data})

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
        vacuna_hepatitis_a = 'Recibida'
        vacuna_hepatitis_b = 'Recibida'
        influenza_estacionaria = 'Recibida'
        fiebre_amarilla = 'Recibida'
        sarampion = ''
        datos_filas_json = request.GET.get('datos_filas')
        datos_filas = json.loads(datos_filas_json) if datos_filas_json else []
        datos_filas_json_hepatitis = request.GET.get('datos_filas_hepatitis')
        datos_filas_hepatitis = json.loads(datos_filas_json_hepatitis) if datos_filas_json_hepatitis else []
        datos_filas_json_hepatitisb = request.GET.get('datos_filas_hepatitisb')
        datos_filas_hepatitisb = json.loads(datos_filas_json_hepatitisb) if datos_filas_json_hepatitisb else []

        datos_filas_json_influenza = request.GET.get('datos_filas_influenza')
        datos_filas_influenza = json.loads(datos_filas_json_influenza) if datos_filas_json_influenza else []

        datos_filas_json_fiebre = request.GET.get('datos_filas_fiebre')
        datos_filas_fiebre = json.loads(datos_filas_json_fiebre) if datos_filas_json_fiebre else []

        datos_filas_json_sarampion = request.GET.get('datos_filas_sarampion')
        datos_filas_sarampion = json.loads(datos_filas_json_sarampion) if datos_filas_json_sarampion else []

        print("datos_filas", datos_filas)
        print("datos_filas_hepatitis", datos_filas_hepatitis)
        print("datos_filas_hepatitisb", datos_filas_hepatitisb)
        print("datos_filas_influenza", datos_filas_influenza)
        print("datos_filas_fiebre", datos_filas_fiebre)


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

        for fila_hepatitis in datos_filas_hepatitis:
            dosis_hepatitis = fila_hepatitis['dosis']
            fecha_str_hepatitis = fila_hepatitis['fecha']
            fecha_hepatitis = datetime.strptime(fecha_str_hepatitis, '%Y-%m-%d').date()
            lote_hepatitis = fila_hepatitis['lote']
            esquema_hepatitis = fila_hepatitis['esquema']
            responsable_hepatitis = fila_hepatitis['responsable']
            establecimiento_hepatitis = fila_hepatitis['establecimiento']
            observaciones_hepatitis = fila_hepatitis['observaciones']

        for fila_hepatitisb in datos_filas_hepatitisb:
            dosis_hepatitisb = fila_hepatitisb['dosis']
            fecha_str_hepatitisb = fila_hepatitisb['fecha']
            fecha_hepatitisb = datetime.strptime(fecha_str_hepatitisb, '%Y-%m-%d').date()
            lote_hepatitisb = fila_hepatitisb['lote']
            esquema_hepatitisb = fila_hepatitisb['esquema']
            responsable_hepatitisb = fila_hepatitisb['responsable']
            establecimiento_hepatitisb = fila_hepatitisb['establecimiento']
            observaciones_hepatitisb = fila_hepatitisb['observaciones']

        for fila_influenza in datos_filas_influenza:
            dosis_influenza = fila_influenza['dosis']
            fecha_str_influenza = fila_influenza['fecha']
            fecha_influenza = datetime.strptime(fecha_str_influenza, '%Y-%m-%d').date()
            lote_influenza = fila_influenza['lote']
            esquema_influenza = fila_influenza['esquema']
            responsable_influenza = fila_influenza['responsable']
            establecimiento_influenza = fila_influenza['establecimiento']
            observaciones_influenza = fila_influenza['observaciones']

        for fila_fiebre in datos_filas_fiebre:
            dosis_fiebre = fila_fiebre['dosis']
            fecha_str_fiebre = fila_fiebre['fecha']
            fecha_fiebre = datetime.strptime(fecha_str_fiebre, '%Y-%m-%d').date()
            lote_fiebre = fila_fiebre['lote']
            esquema_fiebre = fila_fiebre['esquema']
            responsable_fiebre = fila_fiebre['responsable']
            establecimiento_fiebre = fila_fiebre['establecimiento']
            observaciones_fiebre = fila_fiebre['observaciones']

        for fila_sarampion in datos_filas_sarampion:
            dosis_sarampion = fila_sarampion['dosis']
            fecha_str_sarampion = fila_sarampion['fecha']
            fecha_sarampion = datetime.strptime(fecha_str_sarampion, '%Y-%m-%d').date()
            lote_sarampion = fila_sarampion['lote']
            esquema_sarampion = fila_sarampion['esquema']
            responsable_sarampion = fila_sarampion['responsable']
            establecimiento_sarampion = fila_sarampion['establecimiento']
            observaciones_sarampion = fila_sarampion['observaciones']

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

        ###---- INSERT INTO DOSIS VACUNAS ----###
        # Inicializar una lista para almacenar todas las dosis de tetanos
        dosis_list = []
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
                # Define los valores para los parámetros en la tabla DosisVacunaTetano
                params_dosis = (
                    numero_archivo,
                    dosis, fecha, lote, esquema, responsable, establecimiento, observaciones
                )

                # Ejecutar la consulta para la tabla DosisVacunaTetano
                cursor.execute(sql_query_dosis, params_dosis)
                # Agregar cada dosis al listado
                dosis_list.append({
                    'dosis': dosis,
                    'fecha': fecha_str,
                    'lote': lote,
                    'esquema': esquema,
                    'responsable': responsable,
                    'establecimiento': establecimiento,
                    'observaciones': observaciones
                })

        # Inicializar una lista para almacenar todas las dosis de hepatitis
        dosis_list_hepa = []
        with connection.cursor() as cursor_hepatitis:

            sql_query_dosis_hepatitis = """
                INSERT INTO DosisVacunaHepatitisA (
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

            for fila in datos_filas_hepatitis:
                # Accede a las propiedades de cada fila
                dosis_hepatitis = fila['dosis']
                fecha_str_hepatitis = fila['fecha']  # La fecha como cadena en formato 'YYYY-MM-DD'
                fecha_hepatitis = datetime.strptime(fecha_str_hepatitis, '%Y-%m-%d').date()
                lote_hepatitis = fila['lote']
                esquema_hepatitis = fila['esquema']
                responsable_hepatitis = fila['responsable']
                establecimiento_hepatitis = fila['establecimiento']
                observaciones_hepatitis = fila['observaciones']

                params_dosis_hepatitis = (
                    numero_archivo,
                    dosis_hepatitis, fecha_hepatitis, lote_hepatitis, esquema_hepatitis, responsable_hepatitis,
                    establecimiento_hepatitis, observaciones_hepatitis
                )

                cursor_hepatitis.execute(sql_query_dosis_hepatitis, params_dosis_hepatitis)

                dosis_list_hepa.append({
                    'dosis': dosis_hepatitis,
                    'fecha': fecha_str_hepatitis,
                    'lote': lote_hepatitis,
                    'esquema': esquema_hepatitis,
                    'responsable': responsable_hepatitis,
                    'establecimiento': establecimiento_hepatitis,
                    'observaciones': observaciones_hepatitis
                })

        # Inicializar una lista para almacenar todas las dosis de hepatitisb
        dosis_list_hepab = []
        with connection.cursor() as cursor_hepatitisb:
            sql_query_dosis_hepatitisb = """
                            INSERT INTO DosisVacunaHepatitisB (
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

            for fila in datos_filas_hepatitisb:
                # Accede a las propiedades de cada fila
                dosis_hepatitisb = fila['dosis']
                fecha_str_hepatitisb = fila['fecha']  # La fecha como cadena en formato 'YYYY-MM-DD'
                fecha_hepatitisb = datetime.strptime(fecha_str_hepatitisb, '%Y-%m-%d').date()
                lote_hepatitisb = fila['lote']
                esquema_hepatitisb = fila['esquema']
                responsable_hepatitisb = fila['responsable']
                establecimiento_hepatitisb = fila['establecimiento']
                observaciones_hepatitisb = fila['observaciones']

                params_dosis_hepatitisb = (
                    numero_archivo,
                    dosis_hepatitisb, fecha_hepatitisb, lote_hepatitisb, esquema_hepatitisb, responsable_hepatitisb,
                    establecimiento_hepatitisb, observaciones_hepatitisb
                )

                cursor_hepatitisb.execute(sql_query_dosis_hepatitisb, params_dosis_hepatitisb)

                dosis_list_hepab.append({
                    'dosis': dosis_hepatitisb,
                    'fecha': fecha_str_hepatitisb,
                    'lote': lote_hepatitisb,
                    'esquema': esquema_hepatitisb,
                    'responsable': responsable_hepatitisb,
                    'establecimiento': establecimiento_hepatitisb,
                    'observaciones': observaciones_hepatitisb
                })

        # Inicializar una lista para almacenar todas las dosis de influenza
        dosis_list_influenza = []
        with connection.cursor() as cursor_influenza:
            sql_query_dosis_influenza = """
                                        INSERT INTO DosisInfluenzaEstacionaria (
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

            for fila in datos_filas_influenza:
                # Accede a las propiedades de cada fila
                dosis_influenza = fila['dosis']
                fecha_str_influenza = fila['fecha']  # La fecha como cadena en formato 'YYYY-MM-DD'
                fecha_influenza = datetime.strptime(fecha_str_influenza, '%Y-%m-%d').date()
                lote_influenza = fila['lote']
                esquema_influenza = fila['esquema']
                responsable_influenza = fila['responsable']
                establecimiento_influenza = fila['establecimiento']
                observaciones_influenza = fila['observaciones']

                params_dosis_influenza = (
                    numero_archivo,
                    dosis_influenza, fecha_influenza, lote_influenza, esquema_influenza, responsable_influenza,
                    establecimiento_influenza, observaciones_influenza
                )

                cursor_influenza.execute(sql_query_dosis_influenza, params_dosis_influenza)

                dosis_list_influenza.append({
                    'dosis': dosis_influenza,
                    'fecha': fecha_str_influenza,
                    'lote': lote_influenza,
                    'esquema': esquema_influenza,
                    'responsable': responsable_influenza,
                    'establecimiento': establecimiento_influenza,
                    'observaciones': observaciones_influenza
                })

        # Inicializar una lista para almacenar todas las dosis de fiebre
        dosis_list_fiebre = []
        with connection.cursor() as cursor_fiebre:
            sql_query_dosis_fiebre = """
                                        INSERT INTO DosisFiebreAmarilla (
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

            for fila in datos_filas_fiebre:
                # Accede a las propiedades de cada fila
                dosis_fiebre = fila['dosis']
                fecha_str_fiebre = fila['fecha']  # La fecha como cadena en formato 'YYYY-MM-DD'
                fecha_fiebre = datetime.strptime(fecha_str_fiebre, '%Y-%m-%d').date()
                lote_fiebre = fila['lote']
                esquema_fiebre = fila['esquema']
                responsable_fiebre = fila['responsable']
                establecimiento_fiebre = fila['establecimiento']
                observaciones_fiebre = fila['observaciones']

                params_dosis_fiebre = (
                    numero_archivo,
                    dosis_fiebre, fecha_fiebre, lote_fiebre, esquema_fiebre, responsable_fiebre,
                    establecimiento_fiebre, observaciones_fiebre
                )

                cursor_fiebre.execute(sql_query_dosis_fiebre, params_dosis_fiebre)

                dosis_list_fiebre.append({
                    'dosis': dosis_fiebre,
                    'fecha': fecha_str_fiebre,
                    'lote': lote_fiebre,
                    'esquema': esquema_fiebre,
                    'responsable': responsable_fiebre,
                    'establecimiento': establecimiento_fiebre,
                    'observaciones': observaciones_fiebre
                })

        #Inicializar una lista para almacenar todas las dosis de fiebre
        dosis_list_sarampion = []
        with connection.cursor() as cursor_sarampion:
            sql_query_dosis_sarampion = """
                                        INSERT INTO DosisSarampion (
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

            for fila in datos_filas_sarampion:
                # Accede a las propiedades de cada fila
                dosis_sarampion = fila['dosis']
                fecha_str_sarampion = fila['fecha']  # La fecha como cadena en formato 'YYYY-MM-DD'
                fecha_sarampion = datetime.strptime(fecha_str_sarampion, '%Y-%m-%d').date()
                lote_sarampion = fila['lote']
                esquema_sarampion = fila['esquema']
                responsable_sarampion = fila['responsable']
                establecimiento_sarampion = fila['establecimiento']
                observaciones_sarampion = fila['observaciones']

                params_dosis_sarampion = (
                    numero_archivo,
                    dosis_sarampion, fecha_sarampion, lote_sarampion, esquema_sarampion, responsable_sarampion,
                    establecimiento_sarampion, observaciones_sarampion
                )

                cursor_sarampion.execute(sql_query_dosis_sarampion, params_dosis_sarampion)

                dosis_list_sarampion.append({
                    'dosis': dosis_sarampion,
                    'fecha': fecha_str_sarampion,
                    'lote': lote_sarampion,
                    'esquema': esquema_sarampion,
                    'responsable': responsable_sarampion,
                    'establecimiento': establecimiento_sarampion,
                    'observaciones': observaciones_sarampion
                })

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
            'vacuna_hepatits': vacuna_hepatitis_a,
            'dosis_listtetano': dosis_list,
            'dosis_listhepa': dosis_list_hepa,
            'dosis_list_hepab': dosis_list_hepab,
            'dosis_list_influenza': dosis_list_influenza,
            'dosis_list_fiebre': dosis_list_fiebre,
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
    else:
        return JsonResponse({'error': 'Método no permitido'})



