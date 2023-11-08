from django.db import connections
from django.shortcuts import render
from django.db import connection
import json
from django.contrib.auth.decorators import login_required

@login_required()
def empresa(request):
    # Cambiar la base de datos actual a 'main'
    connection = connections['main']
    # Ejecuta la consulta SQL directamente
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM empresa")
        resultados = cursor.fetchall()

    # Transforma los resultados en una lista de diccionarios
    empresas = [{'nombreempresa': row[4]} for row in resultados]

    # Agrega el JSON al contexto
    context = {
        'empresas_json': empresas  # Ahora es una lista de diccionarios
    }

    # Devuelve la respuesta renderizada
    return render(request, 'empresa.html', context)
