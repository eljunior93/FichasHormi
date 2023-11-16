from fpdf import FPDF
import json
import os
import subprocess
from referencias import *

# Lee datos desde el archivo JSON
with open("postReintegro.json", "r") as json_file:
    data = json.load(json_file)

class PDF(FPDF):
    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-20)

        # Arial italic 8
        self.set_font('Arial', 'I', 12)

pdf = PDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.alias_nb_pages()

pdf.add_page()

# TEXTO
pdf.set_font('Arial', '', 6) 


# 1er encabezado ----

bcol_set(pdf, 'blue')
tfont_size(pdf,7)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'A. DATOS DEL ESTABLECIMIENTO - EMPRESA Y USUARIO', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')

bcol_set(pdf, 'green')
tfont_size(pdf,4.8)
tfont(pdf,'B')
pdf.cell(w = 54, h = 6, txt = 'INSTITUCIÓN DEL SISTEMA O NOMBRE DE LA EMPRESA', border = 1,ln = 2, align = 'L', fill = 1)
tfont(pdf,'')

# Casilla de texto en blanco
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=54, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(60, 13)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=22, h=6, txt='RUC', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(60)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=22, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(81, 13)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=20, h=6, txt='CIIU', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(81)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=20, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(101, 13)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=45, h=6, txt='ESTABLECIMIENTO DE SALUD', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(101)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(146, 13)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=27, h=6, txt='NÚMERO DE HISTORIA \nCLÍNICA', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(146)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=27, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(173, 13)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=27, h=6, txt='NÚMERO DE ARCHIVO', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(173)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=27, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_y(24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=18, h=6, txt='PRIMER APELLIDO', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
#pdf.set_x(25)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(28, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=18, h=6, txt='SEGUNDO APELLIDO', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(28)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(46, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=18, h=6, txt='PRIMER NOMBRE', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(46)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(64, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=18, h=6, txt='SEGUNDO NOMBRE', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(64)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(82, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=9, h=6, txt='SEXO', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(82)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=9, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(91, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=9, h=6, txt='EDAD', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(91)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=9, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(100, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
cell_width = 24
pdf.multi_cell(w=cell_width, h=3, txt='PUESTO DE TRABAJO (CIUO)', border=1, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(100)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(124, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4)
tfont(pdf, 'B')
cell_width = 15
pdf.multi_cell(w=cell_width, h=2, txt='FECHA DEL ÚLTIMO DÍA LABORAL', border=1, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(124)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=15, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(139, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4)
tfont(pdf, 'B')
cell_width = 15
pdf.multi_cell(w=cell_width, h=3, txt='FECHA DE REINGRESO', border=1, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(139)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=15, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(154, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4)
tfont(pdf, 'B')
cell_width = 9
pdf.multi_cell(w=cell_width, h=3, txt='TOTAL (DÍAS)', border=1, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(154)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=9, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(163, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=37, h=6, txt='CAUSA DE SALIDA', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(163)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=37, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# 2do encabezado ----

pdf.set_y(38)
bcol_set(pdf, 'blue')
tfont_size(pdf,7)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'B. MOTIVO DE CONSULTA / CONDICIÓN DE REINTEGRO', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')

# Casilla de texto 
pdf.set_y(41)
bcol_set(pdf, 'white')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
cell_width = 0
pdf.multi_cell(w=cell_width, h=5, txt='', border=1, align='L', fill=1)
tfont(pdf, '')
pdf.set_y(46)
bcol_set(pdf, 'white')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
cell_width = 0
pdf.multi_cell(w=cell_width, h=5, txt='', border=1, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto 
pdf.set_y(41)
bcol_set(pdf, 'white')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
cell_width = 12
pdf.multi_cell(w=cell_width, h=2, txt='Descripción', border=0, align='L', fill=1)
tfont(pdf, '')

# 3er encabezado ----

pdf.set_y(54)
bcol_set(pdf, 'blue')
tfont_size(pdf,7)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'C. ENFERMEDAD ACTUAL', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')

# Casilla de texto 
pdf.set_y(57)
bcol_set(pdf, 'white')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
cell_width = 0
pdf.multi_cell(w=cell_width, h=5, txt='', border=1, align='L', fill=1)
tfont(pdf, '')
pdf.set_y(62)
bcol_set(pdf, 'white')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
cell_width = 0
pdf.multi_cell(w=cell_width, h=5, txt='', border=1, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto 
pdf.set_y(57)
bcol_set(pdf, 'white')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
cell_width = 12
pdf.multi_cell(w=cell_width, h=2, txt='Descripción', border=0, align='L', fill=1)
tfont(pdf, '')

# 4to encabezado ----

pdf.set_y(70)
bcol_set(pdf, 'blue')
tfont_size(pdf,7)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'D. CONSTANTES VITALES Y ANTROPOMETRÍA', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')

# Casilla de texto verde
pdf.set_y(73)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
cell_width = 18
pdf.multi_cell(w=cell_width, h=3, txt='PRESIÓN ARTERIAL', border=1, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_y(79)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(28, 73)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=20, h=6, txt='TEMPERATURA (°C)', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_xy(28,79)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=20, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(48,73)
bcol_set(pdf, 'green')
tfont_size(pdf, 4)
tfont(pdf, 'B')
cell_width = 12
pdf.multi_cell(w=cell_width, h=3, txt='FRECUENCIA CARDÍACA', border=1, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_xy(48,79)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(60, 73)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=32, h=6, txt='SATURACIÓN DE OXÍGENO (O2%)', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_xy(60,79)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=32, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(92, 73)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=26, h=6, txt='FRECUENCIA RESPIRATORIA', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_xy(92,79)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=26, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(118, 73)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=16, h=6, txt='PESO (Kg)', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_xy(118,79)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=16, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(134, 73)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=20, h=6, txt='TALLA (cm)', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_xy(134,79)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=20, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(154,73)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
cell_width = 24
pdf.multi_cell(w=cell_width, h=3, txt='INDICE DE MASA CORPORAL (Kg/m2)', border=1, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_xy(154,79)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(178,73)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
cell_width = 22
pdf.multi_cell(w=cell_width, h=3, txt='PERÍMETRO ABDOMINAL (cm)', border=1, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_xy(178,79)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=22, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# 5to encabezado ----

pdf.set_y(87)
bcol_set(pdf, 'blue')
tfont_size(pdf,7)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'E. EXAMEN FÍSICO REGIONAL', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_y(90)
bcol_set(pdf, 'green')
tfont_size(pdf,4.8)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'REGIONES', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.5)
tfont(pdf, 'B')
pos_x = 10  # Ajusta la posición X según tus necesidades
pos_y = 108.2 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('1. PIEL') + 10
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='1. PIEL', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(15, 93)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='a. Cicatrices', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(39,93)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(15, 98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='b. Tatuajes', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(39,98)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(15, 103)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='c. Piel y Faneras', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(39,103)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.5)
tfont(pdf, 'B')
pos_x = 10  # Ajusta la posición X según tus necesidades
pos_y = 133 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('2. OJOS') + 19
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='2. OJOS', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(15, 108)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='a. Párpados', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(39,108)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(15, 113)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='b. Conjuntivas', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(39,113)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(15, 118)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='c. Pupilas', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(39,118)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(15, 123)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='d. Córneas', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(39,123)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(15, 128)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='e. Motilidad', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(39,128)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.5)
tfont(pdf, 'B')
pos_x = 44  # Ajusta la posición X según tus necesidades
pos_y = 108 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('3. OÍDO') + 9
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='3. OÍDO', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(49, 93)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='a. C. auditivo externo', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(73,93)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(49, 98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='b. Pabellón', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(73,98)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(49, 103)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='c. Tímpanos', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(73,103)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.5)
tfont(pdf, 'B')
pos_x = 44  # Ajusta la posición X según tus necesidades
pos_y = 133 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('4. ORO FARINGE') + 12
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='4. ORO FARINGE', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(49, 108)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='a. Labio', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(73,108)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(49, 113)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='b. Lengua', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(73,113)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(49, 118)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='c. Faringe', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(73,118)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(49, 123)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='d. Amígdalas', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(73,123)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(49, 128)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='e. Dentadura', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(73,128)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.5)
tfont(pdf, 'B')
pos_x = 78  # Ajusta la posición X según tus necesidades
pos_y = 113 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('5. NARIZ') + 13.2
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='5. NARIZ', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(83, 93)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='a. Tabique', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(107,93)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(83, 98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='b. Cornetes', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(107,98)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(83, 103)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='c. Mucosa', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(107,103)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(83, 108)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='d. Senos paranasales', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(107,108)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4)
tfont(pdf, 'B')
pos_x = 78  # Ajusta la posición X según tus necesidades
pos_y = 123 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('6. CUELLO') + 2.5
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='6. CUELLO', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(83, 113)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='a. Tiroides / masas', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(107,113)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(83, 118)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='b. Movilidad', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(107,118)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.4)
tfont(pdf, 'B')
pos_x = 78  # Ajusta la posición X según tus necesidades
pos_y = 133 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('7. TÓRAX') + 3
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='7. TÓRAX', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(83, 123)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='a. Mamas', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(107,123)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(83, 128)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='b. Corazón', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(107,128)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4)
tfont(pdf, 'B')
pos_x = 112  # Ajusta la posición X según tus necesidades
pos_y = 103 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('8. TÓRAX') + 3.4
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='8. TÓRAX', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(117, 93)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='a. Pulmones', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(141,93)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(117, 98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='b. Parrilla Costal', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(141,98)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 3.5)
tfont(pdf, 'B')
pos_x = 112  # Ajusta la posición X según tus necesidades
pos_y = 113 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('9.ABDOMEN') + 2.5
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='9.ABDOMEN', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(117, 103)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='a. Víceras', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(141,103)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(117, 108)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='b. Pared Abdominal', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(141,108)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4)
tfont(pdf, 'B')
pos_x = 112  # Ajusta la posición X según tus necesidades
pos_y = 133 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('10. COLUMNA') + 10.6
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='10. COLUMNA', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(117, 113)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='a. Flexibilidad', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(141,113)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(117, 118)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=10, txt='b. Desviación', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(141,118)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=10, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(117, 128)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=24, h=5, txt='c. Dolor', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(141,128)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4)
tfont(pdf, 'B')
pos_x = 146  # Ajusta la posición X según tus necesidades
pos_y = 103 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('11.PELVIS') + 3
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='11.PELVIS', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(151, 93)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=49, h=5, txt='a. Pelvis', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(195,93)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(151, 98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=49, h=5, txt='b. Genitales', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(195,98)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 3.5)
tfont(pdf, 'B')
pos_x = 146  # Ajusta la posición X según tus necesidades
pos_y = 118.1 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('12.EXTREMIDADES') + 3.5
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='12.EXTREMIDADES', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(151, 103)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=49, h=5, txt='a. Vascula', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(195,103)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(151, 108)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=49, h=5, txt='b. Miembros superiores', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(195,108)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(151, 113)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=49, h=5, txt='c. Miembros inferiores', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(195,113)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Cuadro de texto
pdf.set_y(98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.5)
tfont(pdf, 'B')
pos_x = 146  # Ajusta la posición X según tus necesidades
pos_y = 138 # Ajusta la posición Y según tus necesidades
pdf.set_xy(pos_x, pos_y)
cell_width = pdf.get_string_width('13. NEUROLÓGICO') + 5.5
pdf.rotate(90)
pdf.multi_cell(w=cell_width, h=5, txt='13. NEUROLÓGICO', border=1, align='C', fill=1)
pdf.rotate(0)
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(151, 118)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=49, h=5, txt='a. Fuerza', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(195,118)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(151, 123)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=49, h=5, txt='b. Sensibilidad', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(195,123)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(151, 128)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=49, h=5, txt='c. Marcha', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(195,128)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto verde
pdf.set_xy(151, 133)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=49, h=5, txt='d. Reflejos', border=1, ln=2, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(195,133)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=5, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto 
pdf.set_y(133)
bcol_set(pdf, 'white')
tfont_size(pdf, 4)
tfont(pdf, 'B')
cell_width = 136
pdf.multi_cell(w=cell_width, h=5, txt='CP=CON EVIDENCIA DE PATOLOGÍA: MARCAR "X" Y DESCRIBIR EN LA SIGUIENTE SECCIÓN                                               SP=SIN EVIDENCIA DE PATOLOGÍA: MARCAR "X" Y NO DESCRIBIR', border=1, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto 
pdf.set_y(138)
bcol_set(pdf, 'white')
tfont_size(pdf, 4)
tfont(pdf, 'B')
cell_width = 0
pdf.multi_cell(w=cell_width, h=5, txt='', border=1, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto 
pdf.set_y(143)
bcol_set(pdf, 'white')
tfont_size(pdf, 4)
tfont(pdf, 'B')
cell_width = 0
pdf.multi_cell(w=cell_width, h=5, txt='', border=1, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto 
pdf.set_y(148)
bcol_set(pdf, 'white')
tfont_size(pdf, 4)
tfont(pdf, 'B')
cell_width = 0
pdf.multi_cell(w=cell_width, h=5, txt='', border=1, align='L', fill=1)
tfont(pdf, '')
# Casilla de texto 
pdf.set_y(153)
bcol_set(pdf, 'white')
tfont_size(pdf, 4)
tfont(pdf, 'B')
cell_width = 0
pdf.multi_cell(w=cell_width, h=5, txt='', border=1, align='L', fill=1)
tfont(pdf, '')

# 6to encabezado ----
pdf.set_y(161)
bcol_set(pdf, 'blue')
tfont_size(pdf,7)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'F. RESULTADOS DE EXÁMENES (IMAGEN, LABORATORIO Y OTROS)', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_y(164)
bcol_set(pdf, 'green')
tfont_size(pdf,4.8)
tfont(pdf,'B')
pdf.multi_cell(w = 50, h = 4, txt = 'EXAMEN', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
# Casilla de texto en blanco a la derecha
pdf.set_y(168)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=50, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_y(173)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=50, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_y(178)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=50, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
pdf.set_xy(60,164)
bcol_set(pdf, 'green')
tfont_size(pdf,4.8)
tfont(pdf,'B')
pdf.multi_cell(w = 25, h = 4, txt = 'FECHA (aaaa/mm/dd)', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
# Casilla de texto en blanco a la derecha
pdf.set_xy(60,168)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=25, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(60,173)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=25, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(60,178)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=25, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
pdf.set_xy(85,164)
bcol_set(pdf, 'green')
tfont_size(pdf,4.8)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 4, txt = 'RESULTADO', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
# Casilla de texto en blanco a la derecha
pdf.set_xy(85,168)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=0, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(85,173)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=0, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(85,178)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=0, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_y(183)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=0, h=5, txt='Observaciones:', border=1, ln=2, align='L', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# 7mo encabezado ----
pdf.set_y(191)
bcol_set(pdf, 'blue')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 160, h = 3, txt = 'G. DIAGNÓSTICO                                                                                                                                                              PRE=PRESUNTIVO  DEF=DEFINITIVO', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_y(194)
bcol_set(pdf, 'green')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 3, h = 5, txt = '1', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(13,194)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 157, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_y(199)
bcol_set(pdf, 'green')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 3, h = 5, txt = '2', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(13,199)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 157, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_y(204)
bcol_set(pdf, 'green')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 3, h = 5, txt = '3', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(13,204)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 157, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(170,191)
bcol_set(pdf, 'blue')
tfont_size(pdf,4)
tfont(pdf,'B')
pdf.multi_cell(w = 20, h = 3, txt = 'CIA', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(170,194)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 20, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(170,199)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 20, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(170,204)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 20, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(190,191)
bcol_set(pdf, 'blue')
tfont_size(pdf,4)
tfont(pdf,'B')
pdf.multi_cell(w = 5, h = 3, txt = 'PRE', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(190,194)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 5, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(190,199)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 5, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(190,204)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 5, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(195,191)
bcol_set(pdf, 'blue')
tfont_size(pdf,4)
tfont(pdf,'B')
pdf.multi_cell(w = 5, h = 3, txt = 'DEF', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(195,194)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 5, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(195,199)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 5, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(195,204)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 5, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')

# 8vo encabezado ----
pdf.set_y(212)
bcol_set(pdf, 'blue')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'H. APTITUD MÉDICA PARA EL TRABAJO', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_y(215)
bcol_set(pdf, 'green')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 30, h = 3, txt = 'APTO', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(40,215)
bcol_set(pdf, 'white')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 10, h = 3, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(50,215)
bcol_set(pdf, 'green')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 30, h = 3, txt = 'APTO EN OBSERVACIÓN', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(80,215)
bcol_set(pdf, 'white')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 25, h = 3, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(105,215)
bcol_set(pdf, 'green')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 30, h = 3, txt = 'APTO CON LIMITACIONES', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(135,215)
bcol_set(pdf, 'white')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 20, h = 3, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(155,215)
bcol_set(pdf, 'green')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 30, h = 3, txt = 'NO APTO', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(185,215)
bcol_set(pdf, 'white')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_y(218)
bcol_set(pdf, 'blue')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 30, h = 5, txt = 'Observación', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(40,218)
bcol_set(pdf, 'white')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 5, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_y(223)
bcol_set(pdf, 'blue')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 30, h = 5, txt = 'Limitación', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(40,223)
bcol_set(pdf, 'white')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 5, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_y(228)
bcol_set(pdf, 'blue')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 30, h = 5, txt = 'Reubicación', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(40,228)
bcol_set(pdf, 'white')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 5, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')

# 9no encabezado ----
pdf.set_y(236)
bcol_set(pdf, 'blue')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'I. RECOMENDACIONES Y/O TRATAMIENTO', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_y(239)
bcol_set(pdf, 'white')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 5, txt = 'Descripción', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_y(244)
bcol_set(pdf, 'white')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_y(249)
bcol_set(pdf, 'white')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 5, txt = '', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_y(255)
bcol_set(pdf, 'white')
tfont_size(pdf,5)
tfont(pdf,'B')
pdf.multi_cell(w=cell_width, h=2, txt='CERTIFICO QUE LO ANTERIORMENTE EXPRESADO EN RELACIÓN A MI ESTADO DE SALUD ES VERDAD. SE ME HA INFORMADO LAS MEDIDAS PREVENTIVAS A TOMAR PARA DISMINUIR O MITIGAR LOS RIESGOS RELACIONADOS CON MI ACTIVIDAD LABORAL.', border=0, align='L', fill=1)
tfont(pdf,'')

# 10mo encabezado ----
pdf.set_y(259)
bcol_set(pdf, 'blue')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 150, h = 3, txt = 'J. DATOS DEL PROFESIONAL', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_y(262)
bcol_set(pdf, 'green')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 15, h = 6, txt = 'FECHA', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(25,262)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 12, h = 6, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(37,262)
bcol_set(pdf, 'green')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 10, h = 6, txt = 'HORA', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(47,262)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 12, h = 6, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(59,262)
bcol_set(pdf, 'green')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w=11.5, h=2, txt='NOMBRES Y APELLIDOS', border=1, align='C', fill=1)
tfont(pdf,'')
pdf.set_xy(70,262)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 25, h = 6, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(95,262)
bcol_set(pdf, 'green')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w=14, h=6, txt='CÓDIGO', border=1, align='C', fill=1)
tfont(pdf,'')
pdf.set_xy(109,262)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 14, h = 6, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')
pdf.set_xy(123,262)
bcol_set(pdf, 'green')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w=11.5, h=3, txt='FIRMA Y SELLO', border=1, align='C', fill=1)
tfont(pdf,'')
pdf.set_xy(134,262)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 26, h = 6, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')

# 11vo encabezado ----
pdf.set_xy(165,259)
bcol_set(pdf, 'blue')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'K. FIRMA DEL USUARIO', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')
pdf.set_xy(165,262)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 6, txt = '', border = 1,
         align = 'C', fill = 1)
tfont(pdf,'')

pdf.set_y(270)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 6, txt = 'SNS-MSP / Form. HCU 079 / 2019', border = 0,
         align = 'L', fill = 1)
tfont(pdf,'')

pdf.set_xy(170,270)
bcol_set(pdf, 'white')
tfont_size(pdf,4.5)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 6, txt = 'EVALUACIÓN-REINTEGRO', border = 0,
         align = 'L', fill = 1)
tfont(pdf,'')

# Obtén la ruta del directorio "Documentos"
documentos_path = os.path.join(os.path.expanduser("~"), "Documentos")

# Crea la carpeta "FichasVacunas" dentro de "Documentos" si no existe
fichas_vacunas_path = os.path.join(documentos_path, "FichasReintegro")
os.makedirs(fichas_vacunas_path, exist_ok=True)

# Obtén el valor de 'historia_clinica' del archivo JSON
historia_clinica = data.get('historia_clinica', 'SinHistoriaClinica')

# Define la ruta completa donde deseas guardar el PDF con 'historia_clinica' en el nombre
pdf_filename = f'FormatoReintegro_{historia_clinica}.pdf'
pdf_path = os.path.join(fichas_vacunas_path, pdf_filename)

# Guarda el archivo PDF en la ruta especificada
pdf.output(pdf_path)

# Abre el archivo PDF con el visor de PDF predeterminado del sistema
try:
    subprocess.run(['xdg-open', pdf_path])  # Para sistemas basados en Linux con xdg-open
except OSError:  # Maneja excepciones si xdg-open no está disponible o si no es Linux
    try:
        subprocess.run(['open', pdf_path])  # Para sistemas basados en MacOS
    except OSError:  # Maneja excepciones si open no está disponible o si no es MacOS
        subprocess.run(['start', '', pdf_path], shell=True)  # Para sistemas basados en Windows
